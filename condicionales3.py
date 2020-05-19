#contral alt m abrir consola python
#concatenacion de operadores de comparacions
#and y or
#operador in
edad = -7
if 0 < edad < 100:
 	print("Edad correcta")
else:
	print("Edad incorrecta")


print("Ejercicio salarios")

salario_presidente= int(input("Introduce salario presidente: "))
print("Salario presidente: " +str(salario_presidente))

salario_director= int(input("Introduce salario director: "))
print("Salario presidente: " +str(salario_director))

salario_jefe_area= int(input("Introduce salario Jefe Area: "))
print("Salario presidente: " +str(salario_jefe_area))

salario_administrativo= int(input("Introduce salario Administrativo: "))
print("Salario presidente: " +str(salario_administrativo))


if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("Todo funciona corectamente")
else:
	print("Algo falla")
