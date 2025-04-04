#Big O(n * m)
#n=1
#m=5
#Big O(1 * 5)= 5
def iteracao(n, m):
    for i in range(n):
        for j in range(m):
            print(i, j)

iteracao(1, 5)