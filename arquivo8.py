#Busca binaria recursiva
import random as rd
n=[]
for i in range(1024):
    n.append(rd.randint(0, 100))
lista= sorted(n)

print(lista)

def BuscaBinaria(n, inicio, fim, num):
    # caso base para erro
    if inicio > fim:
        return -1

    meio = int((inicio + fim)/2)

    if num > n[meio]:
        inicio= meio+1
        return BuscaBinaria(n, inicio, fim, num)
    elif num < n[meio]:
        fim = meio-1
        return BuscaBinaria(n, inicio, fim, num)
    # caso base para acerto
    else:
        return meio



#n=[1, 2, 3, 4, 5, 6, 7, 8]
inicio=0
fim= len(lista)-1
num= 0
print(BuscaBinaria(lista, inicio, fim, num))