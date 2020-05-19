#dentro de un bucle
#continue: salta a la siguiente iteracion del bucle
#pass: devuelve null, como si no ejecutara el bucle
#else: de forma similar al condicional

for letra in "Python":
	if letra =="h":
		continue
	print("Viendo la letra: "+ letra)

#contar las letras sin espacios
nombre="Pildoras Informaticas"
print(len(nombre))
contador=0
for i in nombre:

	if i ==" ":
		continue
	contador+=1
print(contador)

#pass
class miclase:
	pass # Para implementar mas tarde


#else
email=input("Introduce tu email")
for i in email:
	if i=="@":
		arroba =True
		break
#cuando ya haya recorrido todo el bucle
else:
	arroba=False

print(arroba)

