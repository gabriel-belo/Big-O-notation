#O(log n) iterativo
def log(n):
    while n > 1:
        print(n)
        n= int(n/2)


log(8)