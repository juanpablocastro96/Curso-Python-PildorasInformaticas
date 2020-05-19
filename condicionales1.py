print("Programa de evaluación de notas de alumnos")
nota_alumno = int(input())
def evaluacion(nota):
	#aprobado o suspenso 1-10
	valoracion = "Aprobado"
	if nota < 5:
		valoracion = "Suspenso"
	return valoracion


print(evaluacion(nota_alumno))

#para que sublime text deje introducir por teclado hay que abrir la consola de python en sublime text
#una variable es accesible dentro de un ambito(depende donde se declaran las variables)