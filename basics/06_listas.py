
import os 

os.system("clear") #Limpiar la consola para mejor visualización

#creacion de listas

lista1 = [1, 2, 3, 4, 5] #lista de enteros
lista2 = ["manzana", "banano"] #lista de strings
lista3 = [1, "Hola", 3.14, True] #lista mixta

lista_vacia = [] #lista vacia   

lista_de_listas = [[1, 2], [3, 4], [5, 6]] #lista de listas

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #matriz de 3x3
print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matriz)

#acceder a elementos de la lista

print(lista2[0]) #manzana

#acceder a ultimo elemento de la lista
print(lista2[-1]) #banano

print(lista_de_listas[1][0]) #3
print(matriz[2][1]) #8

#slicing (rebanado) de listas

lista1 = [1, 2, 3, 4, 5]
print(lista1[1:4]) # [2, 3, 4]
