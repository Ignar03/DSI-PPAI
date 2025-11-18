import sqlite3
import os, sys

def seed():
    connection = sqlite3.connect("sismos.db")
    cursor = connection.cursor()

    # Tabla Empleados
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Empleados (
            legajo TEXT PRIMARY KEY,
            apellido TEXT NOT NULL,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL,
            telefono TEXT NOT NULL,
            nombreRol TEXT NOT NULL,
            FOREIGN KEY (nombreRol) REFERENCES Roles(nombre)
        )
        """
    )

    # Tabla Roles
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Roles (
            nombre TEXT PRIMARY KEY,
            descripcion TEXT
        )
        """
    )
    
    # Tabla Estaciones
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Estaciones (
            codigoEstacion TEXT PRIMARY KEY,
            latitud FLOAT,
            longitud FLOAT,
            nombre TEXT,
            fechaSolicitudCertificacion TEXT,
            documentoCertificacionAdq TEXT,
            nroCertificacionAdquisicion TEXT
        )
        """
    )

    # Tabla Usuarios
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Usuarios (
            nombre TEXT PRIMARY KEY,
            contraseña TEXT NOT NULL,
            legajoEmpleado TEXT NOT NULL,
            FOREIGN KEY (legajoEmpleado) REFERENCES Empleados(legajo)
        )
        """
    )

    # Tabla Sesiones
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Sesiones (
            codigoSesion INTEGER PRIMARY KEY AUTOINCREMENT,
            fechaInicionSesion TEXT NOT NULL,
            fechaFinSesion TEXT,
            nombreUsuario TEXT NOT NULL,
            FOREIGN KEY (nombreUsuario) REFERENCES Usuarios(nombre)
        )
        """
    )

    # Tabla Sismografo
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Sismografos (
            codigoSismografo TEXT PRIMARY KEY,
            codigoEstacion TEXT NOT NULL,
            FOREIGN KEY (codigoEstacion) REFERENCES Estaciones(codigoEstacion)
        )
        """
    )
    
    # Tabla Estado
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Estados (
            codigoEstado INTEGER PRIMARY KEY AUTOINCREMENT,
            ambito TEXT,
            nombre TEXT
        )
        """
    )

    # Tabla Cambios Estado
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS CambiosEstado (
            codigoCambioEstado INTEGER PRIMARY KEY AUTOINCREMENT,
            fechaHoraInicio TEXT NOT NULL,
            fechaHoraFin TEXT,
            responsableCambio TEXT NOT NULL,
            codigoEstado INTEGER NOT NULL,
            FOREIGN KEY (responsableCambio) REFERENCES Usuarios(nombre),
            FOREIGN KEY (codigoEstado) REFERENCES Estados(codigoEstado)
        )
        """
    )

    # Tabla CambiosEstadoSismografo
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS CambiosEstadoSismografo (
            codigoSismografo TEXT,
            codigoCambioEstado INTEGER,
            PRIMARY KEY (codigoSismografo, codigoCambioEstado),
            FOREIGN KEY (codigoSismografo) REFERENCES Sismografos(codigoSismografo),
            FOREIGN KEY (codigoCambioEstado) REFERENCES CambiosEstado(codigoCambioEstado)
        )
        """
    )

    # Tabla Motivo Tipo
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS MotivoTipo (
            codigoMotivoTipo INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            descripcion TEXT
        )
        """
    )

    # Tabla Motivo Fuera Servicio
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS MotivoFueraServicio (
            codigoMotivoFueraDeServicio INTEGER PRIMARY KEY AUTOINCREMENT,
            comentario TEXT,
            codigoMotivoTipo INTEGER NOT NULL,
            FOREIGN KEY (codigoMotivoTipo) REFERENCES MotivoTipo(codigoMotivoTipo)
        )
        """
    )

    # Tabla CambiosEstadoMotivoFueraServicio
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS CambiosEstadoMotivoFueraServicio (
            codigoCambioEstado INTEGER NOT NULL,
            codigoMotivoFueraDeServicio INTEGER  NOT NULL,
            PRIMARY KEY (codigoCambioEstado, codigoMotivoFueraDeServicio),
            FOREIGN KEY (codigoCambioEstado) REFERENCES CambiosEstado(codigoCambioEstado),
            FOREIGN KEY (codigoMotivoFueraDeServicio) REFERENCES MotivoFueraServicio(codigoMotivoFueraDeServicio)
        )
        """
    )

    # Tabla Ordenes de Inspeccion
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS OrdenesInspeccion (
            numeroOrden INTEGER PRIMARY KEY,
            fechaHoraInicio TEXT NOT NULL,
            fechaHoraCierre TEXT,
            fechaHoraFinalizacion TEXT,
            observacionCierre TEXT,
            codigoEstado INTEGER NOT NULL,
            legajo TEXT NOT NULL,
            codigoEstacion TEXT NOT NULL,
            FOREIGN KEY (codigoEstado) REFERENCES Estados(codigoEstado),
            FOREIGN KEY (legajo) REFERENCES Empleados(legajo),
            FOREIGN KEY (codigoEstacion) REFERENCES Estaciones(codigoEstacion)
        )
        """
    )
    
    connection.commit()
    connection.close()


def insert_data():
    connection = None
    try:
        connection = sqlite3.connect("sismos.db")
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()

        # Roles
        roles_data = [
            ('RI', 'Responsable de Inspección'),
            ('RR', 'Responsable de Reparación'),
            ('OP', 'Operario'),
            ('AN', 'Analista de datos sísmicos'),
        ]
        cursor.executemany("INSERT INTO Roles (nombre, descripcion) VALUES (?, ?)", roles_data)

        # Estaciones
        estaciones_data = [
            ('EST01', -31.4135, -64.1811, 'Córdoba Centro', '2023-01-15', 'cert01.pdf', 'CERT-001'),
            ('EST02', -32.9468, -60.6393, 'Rosario',        '2023-02-20', 'cert02.pdf', 'CERT-002'),
            ('EST03', -34.6037, -58.3816, 'Buenos Aires',   '2023-03-10', 'cert03.pdf', 'CERT-003'),
            ('EST04', -24.1858, -65.3006, 'Jujuy',          '2023-04-05', 'cert04.pdf', 'CERT-004'),
            ('EST05', -51.6226, -69.2181, 'Río Gallegos',   '2023-05-12', 'cert05.pdf', 'CERT-005')
        ]
        cursor.executemany("""
            INSERT INTO Estaciones 
            (codigoEstacion, latitud, longitud, nombre, fechaSolicitudCertificacion, documentoCertificacionAdq, nroCertificacionAdquisicion) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, estaciones_data)

        # Estados
        estados_data = [
            ('OI', 'Pendiente a Realización'),  # ID 1
            ('OI', 'En Curso'),                 # ID 2
            ('OI', 'Cerrada'),                  # ID 3
            ('S',  'En Servicio'),              # ID 4
            ('S',  'Fuera de Servicio'),        # ID 5
            ('OI', 'Completamente Realizada')   # ID 6
        ]
        cursor.executemany("INSERT INTO Estados (ambito, nombre) VALUES (?, ?)", estados_data)

        # MotivoTipo
        motivo_tipo_data = [
            ('Falla Hardware', 'Problema físico en el equipo'),
            ('Falla Software', 'Error en el programa'),
            ('Mantenimiento Programado', 'Tareas rutinarias'),
            ('Vandalismo', 'Daño por terceros'),
            ('Conectividad', 'Problemas de red')
        ]
        cursor.executemany("INSERT INTO MotivoTipo (nombre, descripcion) VALUES (?, ?)", motivo_tipo_data)

        # Empleados
        empleados_data = [
            ('LEG001', 'Gomez',  'Laura', 'lgomez@mail.com', '3511001000', 'AN'),
            ('LEG002', 'Perez',  'Martin','mperez@mail.com', '3512002000', 'RR'),
            ('LEG004', 'Sosa',   'Diego', 'dsosa@mail.com',  '3514004000', 'RR'),
            ('LEG005', 'Ramos',  'Julia', 'jramos@mail.com', '3515005000', 'OP'),
            ('LEG006', 'Pancho', 'Odonel', 'podonel@mail.com', '3515005000', 'RR')
        ]
        cursor.executemany("""
            INSERT INTO Empleados (legajo, apellido, nombre, email, telefono, nombreRol) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, empleados_data)

        # Usuarios
        usuarios_data = [
            ('lauraG', 'pass1', 'LEG001'),
            ('martinP','pass2', 'LEG002'),
            ('diegoS', 'pass4', 'LEG004'),
            ('juliaR', 'pass5', 'LEG005')
        ]
        cursor.executemany("""
            INSERT INTO Usuarios (nombre, contraseña, legajoEmpleado)
            VALUES (?, ?, ?)
        """, usuarios_data)

        # Sismografos
        sismografos_data = [
            ('SIS01', 'EST01'),
            ('SIS02', 'EST02'),
            ('SIS03', 'EST03'),
            ('SIS04', 'EST04'),
            ('SIS05', 'EST05')
        ]
        cursor.executemany("""
            INSERT INTO Sismografos (codigoSismografo, codigoEstacion)
            VALUES (?, ?)
        """, sismografos_data)

        # Motivo Fuera Servicio
        motivo_fs_data = [
            ('Corte de energía', 1),
            ('Error en módulo v2', 2),
            ('Mantenimiento rutina', 3),
            ('Golpe en gabinete', 4),
            ('Perdida enlace satelital', 5)
        ]
        cursor.executemany("""
            INSERT INTO MotivoFueraServicio (comentario, codigoMotivoTipo)
            VALUES (?, ?)
        """, motivo_fs_data)

        # Sesiones
        sesiones_data = [
            ('2025-11-10 10:00', 0, 'diegoS')
        ]
        cursor.executemany("""
            INSERT INTO Sesiones (fechaInicionSesion, fechaFinSesion, nombreUsuario)
            VALUES (?, ?, ?)
        """, sesiones_data)

        # Ordenes Inspeccion
        ordenes_data = [
            # (numero, inicio, cierre, finalizacion, obs, estado, legajo, estacion)
            
            (3001, '2025-11-05 08:00', 0, 0, None, 1, 'LEG004', 'EST01'),
            
            (3002, '2025-11-06 09:00', 0, 0, None, 6, 'LEG004', 'EST02'),
            
            (3003, '2025-11-07 10:00', '2025-11-07 11:00', '2025-11-07 12:00', 'OK', 3, 'LEG004', 'EST03'),
            
            (3004, '2025-11-08 14:00', '2025-11-08 15:00', 0, None, 2, 'LEG004', 'EST04'),
            
            (3005, '2025-11-09 16:00', '2025-11-08 15:00', 0, None, 6, 'LEG001', 'EST05')
        ]
        cursor.executemany("""
            INSERT INTO OrdenesInspeccion 
            (numeroOrden, fechaHoraInicio, fechaHoraCierre, fechaHoraFinalizacion, observacionCierre, codigoEstado, legajo, codigoEstacion)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, ordenes_data)

        # Cambios Estado
        cambios_estado_data = [
            # (fechaInicio, fechaFin, responsable, codigoEstado)
            
            # ID 1
            ('2025-11-01 08:00', 0, 'diegoS', 1), # 'Pendiente a Realización'
            
            # ID 2
            ('2025-11-02 09:00', 0, 'diegoS', 5), # 'Fuera de Servicio'
            
            # ID 3
            ('2025-11-04 11:00', 0, 'diegoS', 2), # 'En Curso'
            
            # ID 4
            ('2025-11-05 12:00', 0, 'lauraG', 5)  # 'Fuera de Servicio'
        ]
        cursor.executemany("""
            INSERT INTO CambiosEstado (fechaHoraInicio, fechaHoraFin, responsableCambio, codigoEstado)
            VALUES (?, ?, ?, ?)
        """, cambios_estado_data)

        # Cambios Estado Sismografo
        cambios_sismo_data = [
            ('SIS01', 1),
            ('SIS02', 2),
            ('SIS03', 3),
            ('SIS04', 4),
        ]
        cursor.executemany("""
            INSERT INTO CambiosEstadoSismografo (codigoSismografo, codigoCambioEstado)
            VALUES (?, ?)
        """, cambios_sismo_data)

        # CambiosEstadoMotivoFueraServicio
        # Ahora es lógicamente correcto (IDs 2 y 4 son 'Fuera de Servicio')
        cambios_motivo_data = [
            (2, 1),
            (2, 2),
            (4, 3),
            (4, 4),
        ]
        cursor.executemany("""
            INSERT INTO CambiosEstadoMotivoFueraServicio 
            (codigoCambioEstado, codigoMotivoFueraDeServicio)
            VALUES (?, ?)
        """, cambios_motivo_data)

    except sqlite3.Error as e:
        print(f"Error al insertar datos: {e}", file=sys.stderr)
        if connection:
            connection.rollback()
    else:
        print("Datos insertados correctamente.")
        connection.commit()
    finally:
        if connection:
            connection.close()


# -------------------------
# EJECUCIÓN
# -------------------------

if os.path.exists("sismos.db"):
    os.remove("sismos.db")
    print("Base de datos anterior eliminada.")

seed()
insert_data()