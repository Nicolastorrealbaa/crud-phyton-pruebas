Algoritmo taller_gratuito
	Definir edad Como Entero
	definir inscrito Como cadena
	escribir "Bienvenido, ingrese su edad: "
	leer edad 
	si edad >= 18 Entonces
		escribir "¿Esta inscrito en el taller?: (si/no) "
		leer inscrito
		si inscrito es "no" Entonces
			Escribir "inscripcion aceptada"
		sino
			Escribir "ya esta inscrito"
		FinSi
	SiNo
		Escribir "Debe ser mayor de edad para poder inscribirse"
	finsi
	escribir "programa finalizado"
	
FinAlgoritmo
