#O(n!)

def f(n):
    if n == 0:
        print('*' * 10)
        return

    for i in range(n):
        f(n-1)

print(f(3))