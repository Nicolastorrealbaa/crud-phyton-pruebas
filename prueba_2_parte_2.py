from random import randint

continuar = True

while continuar:
    try:
        limite_inferior = int(input("Ingrese limite inferior: "))
        limite_superior = int(input("Ingrese limite superior: "))

        if limite_inferior >= limite_superior:
            print("Error: el limite inferior debe ser menor que el limite superior")

        else:
            continuar = False

    except:
        print("Debe ingresar solo numeros")

numero = randint(limite_inferior, limite_superior)

if numero % 2 != 0:
    if numero + 1 <= limite_superior:
        numero_final = numero + 1
    else:
        numero_final = numero - 1
else:
    numero_final = numero

intentos = 1

intento1 = 0
intento2 = 0

while intentos <= 3:
    try:
        if intentos == 1:
            numero_usuario = int(input("Intente adivinar: "))
        elif intentos == 2:
            numero_usuario = int(input("Intente de nuevo: "))
        else:
            numero_usuario = int(input("Intente la ultima vez: "))
    except:
        print("Debe ingresar un numero")
        continue
    if numero_usuario == numero_final:
        print("Felicitaciones, pudiste adivinar.")
        break
    if numero_usuario < numero_final:
        print("El numero es mayor.")
    else:
        print("El numero es menor.")
    if intentos == 1:
        intento1 = numero_usuario
    elif intentos == 2:
        intento2 = numero_usuario

        distancia1 = abs(numero_final - intento1)
        distancia2 = abs(numero_final - intento2)

        print("Te dare una pista:")
        if distancia1 < distancia2:
            print("El numero que buscas esta mas cerca de",
                  intento1,
                  "que de",
                  intento2)
        elif distancia2 < distancia1:
            print("El numero que buscas esta mas cerca de",
                  intento2,
                  "que de",
                  intento1)
        else:
            print("Ambos intentos estuvieron igual de cerca")

    intentos += 1

if intentos > 3:
    print("Perdiste.")
    print("El numero era:", numero_final)