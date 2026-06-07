Algoritmo menu
definir actividad, opiciones como cadena 
definir tiempo, opciones, contador, actividades, sumador Como Entero
escribir "registro act diarias, escoja la opcion que necesita"
escribir " ----------------------------------------------"
escribir "1_registrar actividades"
escribir "2_mostrar analisis de tiempo"
escribir "3_salir"
leer opciones 
mientras opciones <> 3 hacer 
	si opciones == 1 Entonces
		actividades = 0 
		tiempo = 0 
		escribir "solo puede escribir 3 actividades"
		mientras actividades < 3 hacer
			actividades = actividades + 1
			escribir "cantidad de actividades: "
			leer actividades
			escribir "escriba el nombre de la actividad" 
			leer actividad 
			escribir "escriba el tiempo de la actividad"
			leer tiempo 
			
		FinMientras
	finsi		
FinMientras
    Escribir "fin del registro"
	
FinAlgoritmo
