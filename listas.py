miLista = ["Marta","Pepe","Paco","Carmen"]
print(miLista[:])
print(miLista[:3])
print(miLista[1:3])
print(miLista[2:])
#el primer indice indicado siempre lo incluye pero el ultimo no
print(miLista[1:])
print(miLista[3:])

#agregar
miLista.append("Fercho") # agrega al final
miLista.insert(2,"Venus")#primer numero el indice en el que ira
miLista.extend(["Kley","Sasha"]) #concatenar dos listas 

#devolver el indice
print(miLista.index("Fercho"))
#si hay elementos iguales devuelve el primero que encuentra

#comprobar si hay un elemento t/f
print("Pepe" in miLista)

miLista = ["Mi", 5, 3.4, True]


#ELiminar elementos, especificando el elemento
miLista.remove("Mi")

#eliminar el ultimo
miLista.pop()



#unir listas 
miLista2 = ["Mi", 5, 3.4, True]
miLista3 = ["Mi", 6, .4, False]
miLista4 = miLista2+miLista3


#repetir lista
miLista = ["Mi", 5, 3.4, True]*3


