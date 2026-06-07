v_medicamento = 60000
despacho = 8000

print("----- Tienda -----")

continuar = True
while continuar:
    try:
        edad = int(input("Ingrese su edad: "))
        continuar = False
    except:
        print("Debe ingresar un numero")

continuar = True
while continuar:
    tramo_cliente = input("Ingrese su tramo (A,B,C,D): ").upper()

    if tramo_cliente == "A" or tramo_cliente == "B" or tramo_cliente == "C" or tramo_cliente == "D":
        continuar = False
    else:
        print("Debe ingresar una opcion valida")

valor_medicamento = v_medicamento
valor_despacho = despacho

if edad <= 30 and (tramo_cliente == "A" or tramo_cliente == "B"):
    valor_medicamento = v_medicamento - (v_medicamento * 18/100)
    valor_despacho = despacho - (despacho * 10/100)

elif edad <= 30 and (tramo_cliente == "C" or tramo_cliente == "D"):
    valor_medicamento = v_medicamento - (v_medicamento * 12/100)

elif edad >= 31 and edad <= 60 and (tramo_cliente == "A" or tramo_cliente == "B"):
    valor_medicamento = v_medicamento - (v_medicamento * 12/100)
    if edad >= 55:
        valor_despacho = despacho - (despacho * 15/100)
    else:
        valor_despacho = despacho - (despacho * 10/100)
elif edad >= 31 and edad <= 60 and (tramo_cliente == "C" or tramo_cliente == "D"):
    valor_medicamento = v_medicamento - (v_medicamento * 8/100)
elif edad > 60 and (tramo_cliente == "A" or tramo_cliente == "B"):
    valor_despacho = despacho - (despacho * 15/100)

valor_total = valor_medicamento + valor_despacho

print("El valor del medicamento es: $", int(valor_medicamento))
print("El valor del despacho es: $", int(valor_despacho))
print("Valor total: $", int(valor_total))
# Prueba 2