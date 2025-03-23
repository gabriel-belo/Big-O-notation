#Busca binaria iterativa
def buscaBinaria(n):
    inicio=0
    fim= len(n)-1
    num= 6
    while n != num:
        meio= int((inicio + fim) / 2)
        if num > n[meio]:
            inicio = meio
        elif num < n[meio]:
            fim = meio
        else:
            return True

print(buscaBinaria([1, 2, 3, 4, 5, 6, 7, 8]))