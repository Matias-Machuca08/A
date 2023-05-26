lista = [1,2,3,4] #indice inicial del cero
lista2 = ["hola","chao", True, 1.5, 100]

print (lista)

print("valor del indice 1 (parte del cero): ", lista [1])
print("valor del indice 3 (parte del cero): ", lista [3])


print("valor del indice 1: ", lista2 [1])
print("valor del indice 4: ", lista2 [4])
print("valor del indice 4: ", lista2 [-1])
print("valor del indice 4: ", lista2 [-2])


print("cantidad de elementos: ", len(lista))

lista.append(100) #back box
print(lista)
print("cantidad de elementos: ", len(lista))

lista.reverse()
print(lista)

lista.insert(2, 500)
print (lista)

lista3=[1000,2000]
# agrega una lista previa a otra
lista.extend(lista3)
print (lista)

print ("Hola")
