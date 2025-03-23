#O(log n)
def logFunc(n):
    if n == 0:
        return print('Done')

    n= int(n/2)

    return logFunc(n)

logFunc(8)