#es un errro en tiempo de ejecucion, que no estaba previsto

def suma(num1,num2):
	return num1+num2

def resta(num1,num2):
	return num1-num2

def multiplica(num1,num2):
	return num1*num2

def divide(num1,num2):
	try:
		return num1/num2
	except ZeroDivisionError:
		print("No se puede dividir entre 0")
		return("Operacion erronea")
opc1=(int(input("Introduce el primer numero: ")))
opc2=(int(input("Introduce el segundo numero: ")))
operacion=input("Introduce la operacion a realizar (suma, resta, multiplica, divide):  ")

if operacion=="suma":
	print(suma(opc1,opc2))

elif operacion=="resta":
	print(resta(opc1,opc2))

elif operacion=="multiplica":
	print(multiplica(opc1,opc2))

elif operacion=="divide":
	print(divide(opc1,opc2))

else:
	print("Operacion no resuelta")
 
print("Operacion ejecutada.Continuacion de ejecucion del programa ")









