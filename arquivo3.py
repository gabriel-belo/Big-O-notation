#Notação O(n²)

def quadratica(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

quadratica(2)