especialistas = 0
residentes = 0

while True:
    try:
        cantidad = int(input("Ingrese cantidad de medicos: "))
        if cantidad > 0:
            break
        else:
            print("¡Registro medico invalido! Ingresa un entero positivo para continuar.")
    except:
        print("¡Registro medico invalido! Ingresa un entero positivo para continuar.")
for i in range(cantidad):
    print(f"\nRegistro medico {i + 1}")
    while True:
        nombre = input("Ingrese nombre profesional: ")
        if len(nombre) >= 6 and " " not in nombre:
            break
        else:
            print("Nombre profesional invalido.")
    while True:
        try:
            experiencia = int(input("Ingrese años de experiencia: "))
            if experiencia >= 0:
                break
            else:
                print("¡Error clinico! Ingresa un numero entero positivo para la experiencia.")
        except:
            print("¡Error clínico! Ingresa un numero entero positivo para la experiencia.")
    if experiencia > 5:
        clasificacion = "Especialista Senior"
        especialistas += 1
    else:
        clasificacion = "Residente Junior"
        residentes += 1
    print("Clasificacion:", clasificacion)
print("\nResumen Final")
print(f"¡El hospital cuenta con {especialistas} Especialistas Senior y {residentes} Residentes Junior! ¡Sistema listo para operar!")