#instalar numoy:
#ir a consola o terminal
#pip install numpy
#pip list

import numpy

arreglo = numpy.array ([1,5,6,7])
print(arreglo)

print("cantidad de dimensiones: ", arreglo.ndim)
print("cantidad de elementos: ", len(arreglo))

arreglo = numpy.array([1,5,6,7,9,110,50,40,3,55])

print("cantidad de dimensiones: ", arreglo.ndim)
print("cantidad de elementos: ", len(arreglo))
print("valor elemento 2: ", arreglo [2]) #indice de inicio: 0
print("cortar areglo: ", arreglo[2:5]) # devuelve el indice 2, 3 y 4
print("cortar areglo: ", arreglo[0:8:2]) # aumenta en 2 rl contador para el indice
print("valor ultimo elemento: ", arreglo[-1]) 
print("valor ante-penultimo elemento: ", arreglo[-3]) 
        #cambiar valor de inicio. por defecto parte del cero
arreglo2 = [i+1 for i in range (0,5)] #crear arreglo con 5 elementos


print(len(arreglo2))
for x in range(len(arreglo2)): ## recorrer un arreglo
    print(arreglo2[x])


#crea un arreglo de 10 elementos y valores desde el 0
arreglo3 = numpy.arange(10)
print(arreglo3)


arreglo4 = arreglo3
print(arreglo4)
arreglo4[0] = 100 #modifica el valor del indice 0
print (arreglo3)

#operaciones con arreglo
arr1 = numpy.array([10,20,30,40,50])
arr2 = numpy.array([1,20,3,40,50])
res=arr1+arr2 #ambos arreglos debem tener la misma cantidad de elementos
print("resultado: ",res)
res= arr1 * arr2
print("resultado: ", res)
print(arr1==arr2)
print(arr1>arr2)
print("sumar los elementos: ", arr1.sum())
print("sumar los elementos: ", arr1.sum())
print("valor menor: ", arr1.min())
print("valor mayor: ", arr1.max())
------------------------------------
import random

arr1 = []

for i in random (10):
    arr1.append (random.randint(0,100))
    print(arr1.append)
