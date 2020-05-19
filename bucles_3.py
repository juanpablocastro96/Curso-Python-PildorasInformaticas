for i in range(5,10,2):#comienza en el 5 termina en el 10 y va de dos en dos
	print(f"valor de la ariable {i}")
	#f nos ayuda a entender que {i} se va sumando unir textos con variables

#funcion ln lingitud de un string
valido=False

email=input("Introduce tu email ")
for i in range(len(email)):#len devuelve 4:0,1,2,3
	if email[i] == "@":
		valido = True

if valido:
	print("Email correcto")
else:
	print("Email incorrecto")