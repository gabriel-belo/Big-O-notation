#Este código tem complexidade de espaço de O(n), pois o espaço ocpado aimenta de forma linear.

def countDown(n):
    if n == 0:
        return
    return countDown(n - 1)