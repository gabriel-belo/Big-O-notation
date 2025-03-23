# Complexidade O(n log n)
def mergeSort(lista):
    if len(lista) < 2:
        return lista  # Caso base: se a lista tiver 0 ou 1 elemento, já está ordenada!

    index_meio = len(lista) // 2  # Usa // para divisão inteira
    lista_esquerda = lista[0:index_meio]
    lista_direita = lista[index_meio:]  # Tira o -1 (ele causava erro e deixava elementos de fora)

    # Chama recursivamente para as duas metades e depois faz o merge
    return merge(mergeSort(lista_esquerda), mergeSort(lista_direita))

def merge(lista_esquerda, lista_direita):
    listaResultado = []
    indiceEsquerda = 0
    indiceDireita = 0

    # Enquanto houver elementos nas duas listas
    while indiceEsquerda < len(lista_esquerda) and indiceDireita < len(lista_direita):
        if lista_esquerda[indiceEsquerda] < lista_direita[indiceDireita]:
            listaResultado.append(lista_esquerda[indiceEsquerda])
            indiceEsquerda += 1
        else:
            listaResultado.append(lista_direita[indiceDireita])
            indiceDireita += 1

    # Adiciona os elementos restantes (de uma das duas listas)
    listaResultado += lista_esquerda[indiceEsquerda:]
    listaResultado += lista_direita[indiceDireita:]

    return listaResultado

# Exemplo de uso
print(mergeSort([12, 3, 16, 6, 5, 1]))
