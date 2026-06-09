import sqlite3

conexion = sqlite3.connect("mgstudio.db")
cursor = conexion.cursor()


#tabla de clientes

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    dni TEXT NOT NULL UNIQUE,
    telefono TEXT NOT NULL,
    fecha_nacimiento DATE,
    activo INTEGER DEFAULT 1
)
""")


#tabla de turnos

cursor.execute("""
CREATE TABLE IF NOT EXISTS turnos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    fecha DATE NOT NULL,
    hora TEXT NOT NULL,
    detalle_servicios TEXT,
    observaciones TEXT,
    estado TEXT DEFAULT 'Reservado',
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(cliente_id)
    REFERENCES clientes(id)
)
""")


#tabla de configuracion de turno

cursor.execute("""
CREATE TABLE IF NOT EXISTS configuracion (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    hora_inicio_manana TEXT,
    hora_fin_manana TEXT,

    hora_inicio_tarde TEXT,
    hora_fin_tarde TEXT,

    intervalo_minutos INTEGER DEFAULT 90
)
""")

conexion.commit()
conexion.close()

print("Base de datos creada correctamente")