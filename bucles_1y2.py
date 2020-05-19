for i in [1,2,3]:
	print("Hola")
for i in ["Primavera ", "Verano", "Otoño", "Invierno"]:
	print(i)


for i in ["Pildoras", "Informaticas", 3]:
	print("Hola", end=" ")#Para que escriba todo en una sola linea, que no lo escriba en diferentes lineas

for i in "hola":
	print(1)
#validar un email en funcion si tiene @ o no(no es el unico parametro)

#aqui toma l i cada uno de los caracteres del email juanpi...
email=False
for i in "juanpihotmail.com":
	if i == "@":
		email = True

if email:#= email==True
	print("Es correcto")
else: 
	print("El email es falso")
		

email2=False
mi_email=input("Introduce tu email: ")
for i in mi_email:
	if i =="@":
		email2=True
	
if email2:
	print("Email es correcto")
else: 
	print("el emails es falso")



#ejercicio

contador = 0
mip_email=input("Introduce tu email: ")
for i in mip_email:
	if i =="@" or i==".":
		contador=contador+1
	
if contador==2:
	print("Email es correcto")
else: 
	print("el emails es falso")

#------------------------------------
for i in range(5):#5 elementos: 0,1,2,3,4
	print("Adios")