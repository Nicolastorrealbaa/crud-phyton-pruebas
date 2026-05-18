v_medicamento = 60000
despacho = 8000
descuento_despacho = despacho * 10/100
descuento_despacho_m55 = despacho * 15/100
tramo_a_b_m30 = v_medicamento * 18/100
tramo_c_d_m30 = v_medicamento * 12/100
tramo_a_b_m60 = v_medicamento * 12/100 
tramo_c_d_m60 = v_medicamento * 8/100

print("----- Tienda -----")

continuar = True
while continuar: 
    try:
        edad = int(input(" ingrese su edad: "))
        continuar = False
    except:
        print("debe ingresar un numero")

continuar = True
while continuar: 
    tramo_cliente = input("ingrese su tramo (A,B,C,D): ").upper()
    if tramo_cliente == "A" or tramo_cliente == "B" or tramo_cliente == "C" or tramo_cliente == "D":
        continuar = False
    else:    
        print("debe ingresar una opcion valida")        
    
if edad <= 30 and (tramo_cliente == "A" or tramo_cliente == "B"): 
    print("El valor del medicamento es: $", int(v_medicamento - tramo_a_b_m30 ))
    print("despacho: $", int(despacho - descuento_despacho))
    print("valor total: $", int(v_medicamento - tramo_a_b_m30 + despacho - descuento_despacho))

elif edad <= 30 and (tramo_cliente == "C" or tramo_cliente == "D"):
    print("El valor del medicamento es: $", int(v_medicamento - tramo_c_d_m30))
    print("despacho: $", int(despacho))
    print("valor total: $", int(v_medicamento - tramo_c_d_m30 + despacho))

elif edad >= 31 and edad <= 60 and (tramo_cliente == "A" or tramo_cliente =="B"):
    if edad >= 55 and edad <= 60 :
        print("El valor del medicamento es: $", int(v_medicamento - tramo_a_b_m60))
        print("El valor del despacho es: $", int(despacho - descuento_despacho_m55))
        print("valor total: $", int(v_medicamento - tramo_a_b_m60 + despacho - descuento_despacho_m55)) 
    else:
        print("El valor del medicamento es: $", int(v_medicamento - tramo_a_b_m60)) 
        print("El valor del despacho es: $", int(despacho - descuento_despacho)) 
        print("valor total: $", int(v_medicamento - tramo_a_b_m60 + despacho - descuento_despacho))
elif edad >= 31 and edad <= 60 and (tramo_cliente == "C" or tramo_cliente =="D"):
    print("El valor del medicamento es: $", int(v_medicamento - tramo_c_d_m60))
    print("El valor del despacho es: $", int(despacho))
    print("valor total: $", int(v_medicamento - tramo_c_d_m60 + despacho))

elif edad > 60 and (tramo_cliente == "A" or tramo_cliente == "B"):
    print("El valor del medicamento es: $", int(v_medicamento))
    print("El valor del despacho es: $", int(despacho - descuento_despacho_m55))
    print("valor total: $", int(v_medicamento + despacho - descuento_despacho_m55))
elif edad > 60  and (tramo_cliente == "C" or tramo_cliente == "D"):
    print("El valor del medicamento es: $", int(v_medicamento))
    print("El valor del despacho es: $", int(despacho))
    print("valor total: $", int(v_medicamento + despacho))
else:
    print("no tiene descuento")