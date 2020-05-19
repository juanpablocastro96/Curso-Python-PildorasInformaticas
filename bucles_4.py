#bucle while (indeterminado)

edad = int(input("Ingrese su edad: "))
while edad<0 or edad>100:
	print("Has introducido una edad negativa, intentalo de nuevo")
	edad = int(input("Ingrese su edad: "))

print("Puedes pasar")
print(f"Edad del pasante {edad}")



#ejemplo dos concepto de importacion
import math
print("Programa de calculo de raiz cuadrada")
numero = int(input("Ingrese un numero: "))
intentos=0
while numero<0:
	print("No se puede hallar la raiz de un numero negativo")
	if intentos == 2:
		print("Has consumido muchos intetntos. El programa ha finalizado.")
		break
	numero = int(input("Introduce un numero por favor "))
	if numero<0:
		intento=intentos+1
if intentos<2:
	soluion=math.sqrt(numero)
	print("La raiz cuadrad de "+ str(numero)+ " es " + str(soluion))
