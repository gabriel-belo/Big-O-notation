#Big O(n³)
def cubo(n):
    for i in range(n): #colunas
        for j in range(n): #linhas
            for k in range(n): #altura
                print(i, j, k)

cubo(3)