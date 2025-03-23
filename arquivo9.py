#O (n log n)

def nLogFunc(n):
    y= n
    while n > 1:
        n= n//2
        for i in range(y):
            print(i+1)

nLogFunc(4)