import numpy as np

#crear una matriz
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])

print("valorde la coordenada 1,1:" , matriz[1,1])
print("valorde la coordenada 2,0:" , matriz[2,0])

for f in range(3):
    for c in range (3):
        print("valor:" , matriz[f,c])

print(matriz)

for fila in range(3):
    for columna in range(3):
        print("fila: ", fila, "columna:", columna, "valor: ", matriz[fila,columna])

matriz1 = np.zeros((4,3))
print(matriz1)

matriz1 = np.ones ((5,6))
print(matriz1)

matriz1 =np.diag((1,3,5,1))
print(matriz1)

print("suma de valores: ", matriz.sum())
print("cant. elemento matriz: ", matriz.size)
print("tamaño matriz: ", matriz.shape)
