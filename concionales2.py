print("Verificación de nota")
nota_usuario = float(input("Introduce tu nota: "))

if nota_usuario < 5.0:
	print("Insuficiente")
elif nota_usuario < 6.0:
	print("Suficiente ")
elif nota_usuario < 7.0:
	print("Bien ")
elif nota_usuario < 9.0:
	print("Notable")
else:
	print("Sobresaliente")
	
