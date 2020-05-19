#POO a objetos
#POP son los antiguos Procedimientos
class coche():
	#estado propiedas y comportmiento
	largoChasis=250
	anchoChasis=120
	ruedas=4
	enMarcha=False


	def arrancar(self):
		self.enMarcha=True

	def estado(self):
		if self.enMarcha:
			return "El coche esta en marcha"
		else:
			return "El coche esta parado"

miCoche=coche()
print(miCoche.largoChasis)
print(miCoche.enMarcha)
print(miCoche.estado())

miCoche.arrancar()
print(miCoche.enMarcha)
print(miCoche.estado())


