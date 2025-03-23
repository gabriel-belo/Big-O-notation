#O(n!)

def f(n):
    if n == 0:
        return print('*' * 10)

    for i in range(n):
        f(n-1)

print(f(10))