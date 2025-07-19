import sqlite3
from constantes import *

def conectar_db():
    conexion = sqlite3.connect(DATABASE_NAME)
    cursor = conexion.cursor()
    return conexion, cursor

def crear_tabla_pelicula():
    conexion, cursor = conectar_db()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pelicula (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            duracion INTEGER,
            genero TEXT
        );
    """)
    conexion.commit()
    conexion.close()

# Llama a la función para asegurar que la tabla exista
crear_tabla_pelicula()

def crear_pelicula(pelicula):
    conexion, cursor = conectar_db()
    datos = (
        pelicula.nombre,
        pelicula.duracion,
        pelicula.genero
    )
    sql = "INSERT INTO pelicula (nombre, duracion, genero) VALUES (?, ?, ?);"
    cursor.execute(sql, datos)
    conexion.commit()
    conexion.close()

def buscar_pelicula(nombre):
    conexion, cursor = conectar_db()
    sql = "SELECT * FROM pelicula WHERE nombre = ?;"
    cursor.execute(sql, (nombre,))
    resultado = cursor.fetchone()
    conexion.close()

    if resultado:
        return {
            'id': resultado[0],
            'nombre': resultado[1],
            'duracion': resultado[2],
            'genero': resultado[3]
        }
    else:
        return None

def eliminar_pelicula(nombre):
    conexion, cursor = conectar_db()
    sql = "DELETE FROM pelicula WHERE nombre = ?;"
    cursor.execute(sql, (nombre,))
    conexion.commit()
    conexion.close()

def listar_peliculas():
    conexion, cursor = conectar_db()
    sql = """
        SELECT pelicula.id, pelicula.nombre, pelicula.duracion, genero.nombre
        FROM pelicula
        JOIN genero ON pelicula.genero = genero.id;
    """
    cursor.execute(sql)
    resultados = cursor.fetchall()
    conexion.close()

    peliculas = []
    for resultado in resultados:
        peliculas.append({
            'id': resultado[0],
            'nombre': resultado[1],
            'duracion': resultado[2],
            'genero': resultado[3]
        })

    return peliculas