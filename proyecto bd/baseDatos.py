import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="La-guerra-23",
    database="libreria2"
)

cursor = conexion.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    fecha_inscripcion DATE NOT NULL,
    estado VARCHAR(20) DEFAULT 'Activo',
    cuota_mensual DECIMAL(10,2) DEFAULT 50.00
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS libros (
    id_libro INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    isbn VARCHAR(20) UNIQUE,
    genero VARCHAR(50),
    año_publicacion INT
);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS prestamos (
    id_prestamo INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_libro INT NOT NULL,
    fecha_prestamo DATE NOT NULL,
    fecha_devolucion_esperada DATE NOT NULL,
    fecha_devolucion_real DATE,
    estado VARCHAR(20) DEFAULT 'Activo',
    multa DECIMAL(10,2) DEFAULT 0.00,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON UPDATE CASCADE,
    FOREIGN KEY (id_libro) REFERENCES libros(id_libro) ON UPDATE CASCADE
);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS pagos (
    id_pago INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    fecha_pago DATE NOT NULL,
    monto DECIMAL(10,2) NOT NULL,
    mes INT NOT NULL,
    año INT NOT NULL,
    estado VARCHAR(20) DEFAULT 'Pendiente',
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON UPDATE CASCADE,
    UNIQUE KEY unico_usuario_mes_año (id_usuario, mes, año)
);
""")
try:
    conexion.start_transaction()
    cursor.execute("""
    INSERT INTO usuarios (nombre, apellido, correo, telefono, fecha_inscripcion) VALUES
    ('Juan', 'Pérez', 'juan.perez@email.com', '555-1234', DATE_SUB(CURDATE(), INTERVAL 10 MONTH)),
    ('María', 'Gómez', 'maria.gomez@email.com', '555-5678', DATE_SUB(CURDATE(), INTERVAL 11 MONTH)),
    ('Carlos', 'Rodríguez', 'carlos.rodriguez@email.com', '555-9012', DATE_SUB(CURDATE(), INTERVAL 9 MONTH)),
    ('Laura', 'Martínez', 'laura.martinez@email.com', '555-3456', DATE_SUB(CURDATE(), INTERVAL 12 MONTH)),
    ('Diego', 'Sánchez', 'diego.sanchez@email.com', '555-7890', DATE_SUB(CURDATE(), INTERVAL 8 MONTH)),
    ('Ana', 'López', 'ana.lopez@email.com', '555-2345', DATE_SUB(CURDATE(), INTERVAL 10 MONTH)),
    ('Pedro', 'Fernández', 'pedro.fernandez@email.com', '555-6789', DATE_SUB(CURDATE(), INTERVAL 11 MONTH)),
    ('Sofía', 'Ruiz', 'sofia.ruiz@email.com', '555-0123', DATE_SUB(CURDATE(), INTERVAL 9 MONTH)),
    ('Miguel', 'Torres', 'miguel.torres@email.com', '555-4567', DATE_SUB(CURDATE(), INTERVAL 12 MONTH)),
    ('Elena', 'Navarro', 'elena.navarro@email.com', '555-8901', DATE_SUB(CURDATE(), INTERVAL 10 MONTH))
    ON DUPLICATE KEY UPDATE
    nombre = VALUES(nombre),
    apellido = VALUES(apellido),
    telefono = VALUES(telefono),
    fecha_inscripcion = VALUES(fecha_inscripcion);
    """)
    cursor.execute("""
    INSERT INTO libros (titulo, autor, isbn, genero, año_publicacion) VALUES
    ('Cien Años de Soledad', 'Gabriel García Márquez', '9780060883287', 'Novela', 1967),
    ('El Principito', 'Antoine de Saint-Exupéry', '9780156012195', 'Fábula', 1943),
    ('Don Quijote', 'Miguel de Cervantes', '9780060934347', 'Novela', 1605),
    ('La Sombra del Viento', 'Carlos Ruiz Zafón', '9780143126492', 'Misterio', 2001),
    ('Rayuela', 'Julio Cortázar', '9780060883270', 'Novela', 1963),
    ('Ficciones', 'Jorge Luis Borges', '9780679722762', 'Cuentos', 1944),
    ('La Ciudad de la Furia', 'Ernesto Sabato', '9780060883264', 'Novela', 1959),
    ('Martín Fierro', 'José Hernández', '9780060883258', 'Poesía', 1872),
    ('La Casa de los Espíritus', 'Isabel Allende', '9780060883241', 'Novela', 1982),
    ('El Túnel', 'Ernesto Sabato', '9780060883235', 'Novela', 1948)
    ON DUPLICATE KEY UPDATE
    titulo = VALUES(titulo),
    autor = VALUES(autor),
    genero = VALUES(genero),
    año_publicacion = VALUES(año_publicacion);
    """)
except:
    conexion.rollback()
    print(f"Error: La transacción ha sido revertida.")

