#O(n), pois uma entrada é utilizada para loop e a outra sío se aplica em uma operação de
#tempo constante
def comparar_com_tamanho(lista1, lista2):
    for _ in range(len(lista1)):  # O(n)
        if len(lista1) > len(lista2): # O(1)
            print("Lista 1 é maior")
        else:
            print("Lista 2 é maior ou igual")