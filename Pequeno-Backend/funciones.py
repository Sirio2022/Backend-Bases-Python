from modelos import Pelicula, Genero, Catalogo
import sql

def agregar_pelicula():
    # Aquí iría la lógica para agregar una película
    # Por ejemplo, podrías pedir al usuario que ingrese el título, director, año, etc.
    nombre_pelicula = str(input("Ingrese el nombre del pelicula: "))
    duracion_pelicula = int(input("Ingrese la duración de la película en minutos: "))
    genero_pelicula = str(input("Ingrese el género de la película: "))

    nueva_pelicula = Pelicula(nombre_pelicula, duracion_pelicula, genero_pelicula)
    sql.crear_pelicula(nueva_pelicula)

def buscar_pelicula():
    nombre_pelicula = str(input("Ingrese el nombre de la película a buscar: "))
    pelicula = sql.buscar_pelicula(nombre_pelicula)

    if pelicula:
        print(f"Pelicula encontrada: {pelicula['nombre']}, Duración: {pelicula['duracion']} minutos, Género: {pelicula['genero']}")
    else:
        print("Pelicula no encontrada.")

def eliminar_pelicula():
    nombre_pelicula = str(input("Ingrese el nombre de la película a eliminar: "))
    sql.eliminar_pelicula(nombre_pelicula)
    print(f"Pelicula '{nombre_pelicula}' eliminada correctamente.")

def listar_peliculas():
    peliculas = sql.listar_peliculas()

    if peliculas:
        print("Lista de películas:")
        for pelicula in peliculas:
            print(f"{pelicula['id']}. {pelicula['nombre']} - {pelicula['duracion']} minutos - {pelicula['genero']}")
    else:
        print("No hay películas registradas.")
