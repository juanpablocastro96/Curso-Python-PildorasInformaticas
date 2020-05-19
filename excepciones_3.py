def divide():
	try:

		op1=float(input("Ingrese el primer numero: "))
		
		op2=float(input("Ingrese el seguno numero: "))


		print("La division es: "*str(op1/op2) )
	#except ValueError:
	#	print("El valor introducido es erroneo")

	#except ZeroDivisionError:

	#	print("NO se puede dividir entre cero")
	except:
		print("Hubo un error")

	

	print("Calculo realizado")
divide()
#lo que pongo despues del finally siempre se ejecuta
#finally por ejemplo que pase lo que pase cerrar la BD