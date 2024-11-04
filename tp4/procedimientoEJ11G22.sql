DELIMITER //

CREATE PROCEDURE GenerarResumenDiario()
BEGIN
    DECLARE linea_produccion VARCHAR(50);
    DECLARE fecha_produccion DATE;
    DECLARE total_producido INT;
    DECLARE finished INTEGER DEFAULT 0;
    
    DECLARE cur_produccion CURSOR FOR
        SELECT 
            LineaProduccion,
            FechaProduccion,
            SUM(CantidadProducida) as TotalProducido
        FROM Produccion
        GROUP BY LineaProduccion, FechaProduccion;
    
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET finished = 1;
    
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SELECT 'Error durante la generación del resumen diario' AS Mensaje;
    END;
    
    START TRANSACTION;
    
    TRUNCATE TABLE ResumenProduccion;
    
    OPEN cur_produccion;
    
    get_produccion: LOOP
        FETCH cur_produccion INTO linea_produccion, fecha_produccion, total_producido;
        
        IF finished = 1 THEN
            LEAVE get_produccion;
        END IF;
        
        INSERT INTO ResumenProduccion (LineaProduccion, FechaProduccion, TotalProducido)
        VALUES (linea_produccion, fecha_produccion, total_producido);
        
    END LOOP get_produccion;
    
    CLOSE cur_produccion;
    
    COMMIT;
    
    
END //

DELIMITER ;