libros = 120
prestamos = 0
prestamos_u = 0
prestamo_devuelto = 0 

print("¡Bienvenido al sistema de gestion de prestamos de la Biblioteca Central!")
while True:
    print("---- menu ---- \n 1_ Libros disponibles  \n 2_ Realizar prestamo \n 3_ Devolver prestamo \n 4_ Historial prestamos \n 5_ Salir")   

    while True:
        try:
            opcion = int(input("Ingrese la opcion: "))
            if opcion > 0 and opcion <= 5:
                break
            else:
                print("Debe ingresar una de las opciones")
        except:
            print("Debe ingresar unas de las opciones")

    if opcion == 1: 
        print(f"Libros disponibles : {libros}")

    if opcion == 2:
        while True:
            try:
                prestamos_u = int(input("Cantidad de libros que desea llevar: ")) 
                if prestamos_u > 0:
                    if prestamos_u <= libros:
                        prestamos = prestamos + prestamos_u
                        libros = libros - prestamos_u
                        print(f"¡Prestamo realizado!, quedan: {libros} libros")
                        break
                    else:
                        print("Lo siento no hay stock")
                else:
                    print("Debe ser un numero mayor valido")
            except:
                print("Debe ingresar un numero valido ")

    if opcion == 3:
        while True:
            try:
                prestamo_devuelto = int(input("Cuantos devuelve?: "))
                if prestamo_devuelto > 0:
                    if prestamo_devuelto <= prestamos:
                        if libros + prestamo_devuelto <= 120:
                            prestamos = prestamos - prestamo_devuelto
                            libros = libros + prestamo_devuelto
                            print(f"Devolvio, {prestamo_devuelto} libros, quedan: {libros} libros")
                            break
                        else:
                            print("Debe ser menor que los libros totales")
                    else:
                        print("Debe ser menor que los libros totales")
                else:
                    print("Debe ser un numero mayor a 0") 
            except:
                print("Debe ser un numero mayor a 0")

    if opcion == 4:
        print(f"Prestamos activo: {prestamos}, quedan: {libros} libros")

    if opcion == 5:
        print("Gracias por utilizar nuestro software, hasta la proxima")
        break
    # Prueba 3