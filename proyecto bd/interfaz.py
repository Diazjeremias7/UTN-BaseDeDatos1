from datetime import datetime, timedelta
from baseDatos import *
def menu_principal():
    seguir = True
    while seguir:
        print("\nGestión de Biblioteca")
        print("1. Gestión de Usuarios")
        print("2. Gestión de Libros")
        print("3. Manejo de Préstamos")
        print("4. Búsqueda y Filtrado")
        print("5. Reporte de Morosos")
        print("6. Modificación de Cuota")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            gestion_usuarios()
        elif opcion == '2':
            gestion_libros()
        elif opcion == '3':
            manejo_prestamos()
        elif opcion == '4':
            busqueda_filtrado()
        elif opcion == '5':
            reporte_morosos()
        elif opcion == '6':
            modificar_cuota()
        elif opcion == '7':
            seguir = False
            return seguir
        else:
            print("Opción inválida. Intente nuevamente.")

def gestion_usuarios():
    seguir = True
    while seguir:
        print("\n--- Gestión de Usuarios ---")
        print("1. Agregar Usuario")
        print("2. Ver Usuarios")
        print("3. Actualizar Usuario")
        print("4. Eliminar Usuario")
        print("5. Volver")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_usuario()
        elif opcion == '2':
            ver_usuarios()
        elif opcion == '3':
            actualizar_usuario()
        elif opcion == '4':
            eliminar_usuario()
        elif opcion == '5':
            seguir = False
            return seguir
        else:
            print("Opción inválida. Intente nuevamente.")

def agregar_usuario():
    try:
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        correo = input("Ingrese correo electrónico: ")
        telefono = input("Ingrese teléfono: ")
        
        consulta = """INSERT INTO usuarios (nombre, apellido, correo, telefono, fecha_inscripcion, estado) 
        VALUES (%s, %s, %s, %s, %s, 'Activo')"""
        valores = (nombre, apellido, correo, telefono, datetime.now().date())
        
        cursor.execute(consulta, valores)
        conexion.commit()
        print("Usuario agregado exitosamente.")
    except:
        print(f"Error al agregar usuario")

def ver_usuarios():
    consulta = "SELECT * FROM usuarios"
    cursor.execute(consulta)
    usuarios = cursor.fetchall()
    
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    
    print("\nUsuarios Registrados")
    for usuario in usuarios:
        print(usuario)

def actualizar_usuario():
    try:
        id_usuario = input("Ingrese ID de usuario a actualizar: ")
        
        consulta_existe = "SELECT * FROM usuarios WHERE id_usuario = %s"
        cursor.execute(consulta_existe, (id_usuario,))
        usuario = cursor.fetchone()
        
        if not usuario:
            print("Usuario no encontrado.")
            return
        
        nombre = input("ingrese nombre: ")
        apellido = input("ingrese apellido: ")
        correo = input("ingrese correo: ")
        telefono = input("ingrese telefono: ")
        estado = input("ingrese estado: ")
        
        consulta = """
        UPDATE usuarios 
        SET nombre = %s, apellido = %s, correo = %s, 
        telefono = %s, estado = %s 
        WHERE id_usuario = %s
        """
        valores = (nombre, apellido, correo, telefono, estado, id_usuario)
        
        cursor.execute(consulta, valores)
        conexion.commit()
        print("Usuario actualizado exitosamente.")
    except mysql.connector.Error as error:
        conexion.rollback()
        print(f"Error al actualizar usuario: {error}")

def eliminar_usuario():
    try:
        id_usuario = input("Ingrese ID de usuario a eliminar: ")
         
        consulta = "DELETE FROM usuarios WHERE id_usuario = %s"
        cursor.execute(consulta, (id_usuario,))
        conexion.commit()
        print("Usuario eliminado exitosamente.")

    except mysql.connector.Error as error:
        print(f"Error al eliminar usuario: {error}")

def gestion_libros():
    seguir = True
    while seguir:
        print("\nGestión de Libros")
        print("1. Agregar Libro")
        print("2. Ver Libros")
        print("3. Actualizar Libro")
        print("4. Eliminar Libro")
        print("5. Volver")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_libro()
        elif opcion == '2':
            ver_libros()
        elif opcion == '3':
            actualizar_libro()
        elif opcion == '4':
            eliminar_libro()
        elif opcion == '5':
            seguir = False
            return seguir
        else:
            print("Opción inválida. Intente nuevamente.")

def agregar_libro():
    try:
        titulo = input("Ingrese título del libro: ")
        autor = input("Ingrese autor del libro: ")
        isbn = input("Ingrese ISBN (opcional): ")
        genero = input("Ingrese género: ")
        año_publicacion = input("Ingrese año de publicación: ")
        
        consulta = """INSERT INTO libros (titulo, autor, isbn, genero, año_publicacion) 
        VALUES (%s, %s, %s, %s, %s)"""
        valores = (titulo, autor, isbn or None, genero, año_publicacion )
        
        cursor.execute(consulta, valores)
        conexion.commit()
        print("Libro agregado exitosamente.")
    except mysql.connector.Error as error:
        print(f"Error al agregar libro: {error}")

def ver_libros():
    try:
        consulta = "SELECT * FROM libros"
        cursor.execute(consulta)
        libros = cursor.fetchall()
        
        if not libros:
            print("No hay libros registrados.")
            return
        
        print("\nLibros Registrados")
        for libro in libros:
            print(libro)
    except:
        print(f"Error al consultar libros")

def actualizar_libro():
    try:
        id_libro = input("Ingrese ID de libro a actualizar: ")
        
        consulta_existe = "SELECT * FROM libros WHERE id_libro = %s"
        cursor.execute(consulta_existe, (id_libro,))
        libro = cursor.fetchone()
        
        if not libro:
            print("Libro no encontrado.")
            return
        
        titulo = input(f"ingrese título: ")
        autor = input(f"ingrese autor ")
        isbn = input(f"ingrese ISBN: ")
        genero = input(f"ingrese género : ")
        año_publicacion = input("ingrese año publicado: ")
        
        consulta = """UPDATE libros SET titulo = %s, autor = %s, isbn = %s, genero = %s, año_publicacion = %s WHERE id_libro = %s"""
        valores = (titulo, autor, isbn, genero, año_publicacion, id_libro)
        
        cursor.execute(consulta, valores)
        conexion.commit()
        print("Libro actualizado exitosamente.")
    except mysql.connector.Error as error:
        print(f"Error al agregar libro: {error}")

def eliminar_libro():
    try:
        id_libro = input("Ingrese ID de libro a eliminar: ")
         
        consulta = "DELETE FROM libros WHERE id_libro = %s"
        cursor.execute(consulta, (id_libro,))
        conexion.commit()
        print("Libro eliminado exitosamente.")

    except mysql.connector.Error as error:
        print(f"Error al eliminar libro: {error}")

def manejo_prestamos():
    seguir = True
    while seguir:
        print("\nManejo de Préstamos")
        print("1. Realizar Préstamo")
        print("2. Devolver Libro")
        print("3. Calcular Multa")
        print("4. Ver Préstamos Activos")
        print("5. Volver")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            realizar_prestamo()
        elif opcion == '2':
            devolver_libro()
        elif opcion == '3':
            calcular_multa()
        elif opcion == '4':
            ver_prestamos_activos()
        elif opcion == '5':
            seguir = False
            return seguir
        else:
            print("Opción inválida proba de nuevo.")

def realizar_prestamo():
    try:
        if conexion.in_transaction:
            conexion.commit()
        
        ver_usuarios()
        id_usuario = input("Ingrese ID de usuario: ")
        
        ver_libros()
        id_libro = input("Ingrese ID de libro: ")
        
        consulta_disponibilidad = "SELECT * FROM libros WHERE id_libro = %s"
        cursor.execute(consulta_disponibilidad, (id_libro,))
        libro = cursor.fetchone()
        print(libro)
        if not libro:
            print("Lo siento, no hay tal libro.")
            return False
        
        consulta_prestamo_existente = """
        SELECT * FROM prestamos 
        WHERE id_libro = %s AND estado = 'Activo'
        """
        cursor.execute(consulta_prestamo_existente, (id_libro,))
        prestamo_existente = cursor.fetchone()
        if prestamo_existente:
            print("Lo siento, este libro ya está prestado.")
            return False
        
        fecha_prestamo = datetime.now().date()
        fecha_devolucion = fecha_prestamo + timedelta(days=14)
        
        consulta_prestamo = """INSERT INTO prestamos (id_usuario, id_libro, fecha_prestamo, fecha_devolucion_esperada, estado) 
        VALUES (%s, %s, %s, %s, 'Activo')"""
        valores_prestamo = (id_usuario, id_libro, fecha_prestamo, fecha_devolucion)
        
        try:
            if conexion.in_transaction:
                conexion.commit()
            
            conexion.start_transaction()
            
            cursor.execute(consulta_prestamo, valores_prestamo)
            
            conexion.commit()
            
            print("Préstamo realizado exitosamente.")
            print(f"Fecha de devolución esperada: {fecha_devolucion}")
            return True
        
        except mysql.connector.Error as transaction_error:
            conexion.rollback()
            print(f"Error al realizar préstamo durante la transacción: {transaction_error}")
            return False
    
    except mysql.connector.Error as error:
        print(f"Error al preparar préstamo: {error}")
        return False
    except Exception as error:
        print(f"Error inesperado: {error}")
        return False

def devolver_libro():
    try:
        if conexion.in_transaction:
            conexion.commit()
        cursor = conexion.cursor(dictionary=True)
        
        ver_prestamos_activos()
        
        id_prestamo = input("Ingrese ID de préstamo a devolver: ")
        
        consulta_prestamo = "SELECT * FROM prestamos WHERE id_prestamo = %s AND estado = 'Activo'"
        cursor.execute(consulta_prestamo, (id_prestamo,))
        prestamo = cursor.fetchone()
        
        if not prestamo:
            print("Préstamo no encontrado o ya devuelto.")
            return
        
        fecha_devolucion_real = datetime.now().date()
                
        consulta_update = """
        UPDATE prestamos 
        SET fecha_devolucion_real = %s, 
            estado = 'Devuelto' 
        WHERE id_prestamo = %s
        """
        
        try:
            if conexion.in_transaction:
                conexion.commit()

            conexion.start_transaction()
            
            cursor.execute(consulta_update, (fecha_devolucion_real, id_prestamo))
                        
            print("Libro devuelto exitosamente.")
        
        except mysql.connector.Error as error:
            conexion.rollback()
            print(f"Error al devolver libro: {error}")
    except Exception as error:
        conexion.rollback()
        print(f"Error inesperado al devolver libro: {error}")

def calcular_multa():
    try:
        id_prestamo = input("Ingrese ID de préstamo para calcular multa: ")
        
        consulta = """SELECT p.id_prestamo, u.nombre, u.apellido, l.titulo, p.multa 
        FROM prestamos p
        JOIN usuarios u ON p.id_usuario = u.id_usuario
        JOIN libros l ON p.id_libro = l.id_libro
        WHERE p.id_prestamo = %s"""
        
        cursor.execute(consulta, (id_prestamo,))
        detalle_multa = cursor.fetchone()
        
        if detalle_multa:
            print("\nDetalle de Multa")
            print(detalle_multa)
        else:
            print("Préstamo no encontrado.")
    
    except:
        print(f"Error al calcular multa")

def ver_prestamos_activos():
    try:
        consulta = """SELECT p.id_prestamo, u.nombre, u.apellido, l.titulo, p.fecha_prestamo, p.fecha_devolucion_esperada
        FROM prestamos p
        JOIN usuarios u ON p.id_usuario = u.id_usuario
        JOIN libros l ON p.id_libro = l.id_libro
        WHERE p.estado = 'Activo'"""
        
        cursor.execute(consulta)
        prestamos = cursor.fetchall()
        
        if not prestamos:
            print("No hay préstamos activos.")
            return
        
        print("\nPréstamos Activos")
        for prestamo in prestamos:
            print(prestamo)
    except:
        print(f"Error al ver préstamos activos")

def busqueda_filtrado():
    while True:
        print("\n--- Búsqueda ---")
        print("1. Buscar Libros por Título")
        print("2. Buscar Libros por Autor")
        print("3. Buscar Usuarios")
        print("4. Volver")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            buscar_libros_por_titulo()
        elif opcion == '2':
            buscar_libros_por_autor()
        elif opcion == '3':
            buscar_usuarios()
        elif opcion == '4':
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def buscar_libros_por_titulo():
    try:
        titulo = input("Ingrese título a buscar: ")
        consulta = "SELECT * FROM libros WHERE titulo LIKE %s"
        cursor.execute(consulta, (f'%{titulo}%',))
        libros = cursor.fetchall()
        
        if not libros:
            print("No se encontraron libros.")
            return
        
        print("\n--- Libros Encontrados ---")
        for libro in libros:
            print(libro)
    except mysql.connector.Error as error:
        print(f"Error en la búsqueda: {error}")

def buscar_libros_por_autor():
    try:
        autor = input("Ingrese autor a buscar: ")
        consulta = "SELECT * FROM libros WHERE autor LIKE %s"
        cursor.execute(consulta, (f'%{autor}%',))
        libros = cursor.fetchall()
        
        if not libros:
            print("No se encontraron libros.")
            return
        
        print("\n--- Libros Encontrados ---")
        for libro in libros:
            print(libro)
    except mysql.connector.Error as error:
        print(f"Error en la búsqueda: {error}")

def buscar_usuarios():
    try:
        nombre = input("Ingrese nombre o parte del nombre a buscar: ")
        consulta = "SELECT * FROM usuarios WHERE nombre LIKE %s OR apellido LIKE %s"
        cursor.execute(consulta, (f'%{nombre}%', f'%{nombre}%'))
        usuarios = cursor.fetchall()
        
        if not usuarios:
            print("No se encontraron usuarios.")
            return
        
        print("\n--- Usuarios Encontrados ---")
        for usuario in usuarios:
            print(usuario)
            print("---")
    except mysql.connector.Error as error:
        print(f"Error en la búsqueda: {error}")

def reporte_morosos():
    try:
        consulta = """
        SELECT u.id_usuario, u.nombre, u.apellido, p.fecha_devolucion_esperada,DATEDIFF(CURDATE(), p.fecha_devolucion_esperada) AS dias_retraso,l.titulo
        FROM prestamos p
        JOIN usuarios u ON p.id_usuario = u.id_usuario
        JOIN libros l ON p.id_libro = l.id_libro
        WHERE p.estado = 'Activo' AND p.fecha_devolucion_esperada < CURDATE()
        ORDER BY dias_retraso DESC
        """
        
        cursor.execute(consulta)
        morosos = cursor.fetchall()
        
        if not morosos:
            print("\nNo hay usuarios morosos.")
            return
        
        print("\n--- Reporte de Morosos ---")
        total_morosos = len(morosos)
        total_dias_retraso = sum(morosidad['dias_retraso'] for morosidad in morosos)
        promedio_dias_retraso = total_dias_retraso / total_morosos if total_morosos > 0 else 0
        
        print(f"Número total de usuarios morosos: {total_morosos}")
        print(f"Promedio de días de retraso: {promedio_dias_retraso:.2f} días\n")
    except Exception as error:
        print(f"Error al generar reporte de morosos: {error}")
def modificar_cuota():
    try:
        id_usuario = input("Ingrese ID de usuario: ")
        mes = input("Ingrese mes (1-12): ")
        año = input("Ingrese año: ")
        nueva_cuota = input("Ingrese nueva cuota: ")
        
        consulta = """
        UPDATE usuarios 
        SET cuota_mensual = %s 
        WHERE id_usuario = %s
        """
        valores = (nueva_cuota, id_usuario)
        
        cursor.execute(consulta, valores)
        conexion.commit()
        print("Cuota modificada exitosamente.")
    except:
        print(f"Error al modificar cuota")

menu_principal()
cursor.close()
conexion.close()