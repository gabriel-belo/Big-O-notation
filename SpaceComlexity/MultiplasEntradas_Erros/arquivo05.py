def processar_multiplas_listas(lista1, lista2, num_iteracoes):
    """Processa duas listas e repete um certo número de vezes."""
    n = len(lista1)
    m = len(lista2)
    for _ in range(num_iteracoes):  # O(p), onde p é num_iteracoes
        for i in range(n):  # O(n)
            print(lista1[i])
        for j in range(m):  # O(m)
            print(lista2[j])