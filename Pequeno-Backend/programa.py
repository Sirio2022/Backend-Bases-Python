import funciones

while True:
    print("Bienvenido al backend de Peliculas\n")
    try:
        opcion = int(input("1. Agregar pelicula\n2. Buscar pelicula\n3. Eliminar pelicula\n4. Listar peliculas\n5. Salir\nSeleccione una opcion: "))

        if opcion == 1:
            print("Agregar pelicula")
            funciones.agregar_pelicula()
        elif opcion == 2:
            print("Buscar pelicula")
            funciones.buscar_pelicula()
        elif opcion == 3:
            print("Eliminar pelicula")
            funciones.eliminar_pelicula()
        elif opcion == 4:
            print("Listar peliculas")
            funciones.listar_peliculas()
        elif opcion == 5:
            print("Saliendo del programa...")
            exit()
        else:
            print("Opción no válida, por favor intente de nuevo.")
    except ValueError:
        print("Entrada no válida, por favor ingrese un número entero.")
