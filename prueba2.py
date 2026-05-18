from random import randint

limite_inferior = int(input("Ingrese el límite inferior: "))
limite_superior = int(input("Ingrese el límite superior: "))

if limite_inferior >= limite_superior:
    print("Error: el límite inferior debe ser menor que el límite superior")

else:
    print("Rango correcto")

    numero = randint(limite_inferior, limite_superior)

    if numero % 2 == 0:
        if numero + 1 <= limite_superior:
            numero_final = numero + 1
        else:
            numero_final = numero - 1
    else:
        numero_final = numero

    intentos = 1
    adivino = False

    intento1 = 0
    intento2 = 0

    while intentos <= 3 and adivino == False:

        numero_usuario = int(input(f"Intento ({intentos}): "))

        if numero_usuario == numero_final:
            print("Felicitaciones, pudiste adivinar.")
            adivino = True

        else:
            if numero_usuario < numero_final:
                print("El número es mayor")
            else:
                print("El número es menor")

        if intentos == 1:
            intento1 = numero_usuario

        elif intentos == 2:
            intento2 = numero_usuario

            distancia1 = abs(numero_final - intento1)
            distancia2 = abs(numero_final - intento2)

            print("Te daré una pista:")

            if distancia1 < distancia2:
                print("El número está más cerca de", intento1, "que de", intento2)

            elif distancia2 < distancia1:
                print("El número está más cerca de", intento2, "que de", intento1)

            else:
                print("Ambos intentos estuvieron igual de cerca")

        intentos += 1

    if adivino == False:
        print("Perdiste")
        print("El número era:", numero_final)