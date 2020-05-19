#distancia superior a 40 km se le da beca
#si tiene mas hermanos >3
#salario familiar<=20.000
#lower() todo minusculas
#upper todo mayusculas
print("Programa de becas:")
distancia_escuela=int(input("Introduce la distancia a la escuela en km"))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el numero de hermanos en el centro"))
print(numero_hermanos)

salario_familiar=int(input("Introduce el salario familiar anual bruto"))
print(salario_familiar)


if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
	print("Tienes derecho a beca")
else:
	print("No tienes derecho a beca")


#escoger una asignatura optativa
print("Programa 2")
print("Asignaturas optativas: Infromatica grafica - Pruebas de software - Usabilidad y accesibilidad")
opcion=input("Escriba la asignatura escogida: ")
asignatura=opcion.lower()
if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
	print("La asignatura escogida es " + asignatura)
else:
	print("Error")

