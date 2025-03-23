#Está função é similar ao exemplo da dentista com a notação Big O(n)

def funcaoLinear(lista):
    for i in range(len(lista)):
        print(10 * lista[i]) #O tempo para o cálculo dé constante

lista=[10, 100, 1000, 10000, 100000]
funcaoLinear(lista)