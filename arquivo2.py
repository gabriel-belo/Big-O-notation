#Este caso temos uma notação Big O(1), pois a quantidade de vezes que o for se repete indifere
#do tamanho da lista
def funcaoLinear(lista):
    for i in range(10):  # Loop fixo, SEM depender do tamanho da lista
        print(10 * lista[i])  # Operação constante O(1)

lista = [10, 100, 1000, 10000, 100000]
funcaoLinear(lista)
