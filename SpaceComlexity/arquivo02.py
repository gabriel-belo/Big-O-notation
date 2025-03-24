#um erro muito comum é acreditar que neste caso temos uma complecidade de O(n²) pois temos dois loops for,
#porém temos uma complexidade O(n) já que os loops não interagem. Na verdade temos O(2n) porém comom ignoramos
#constantes temos O(n).
def twoLoops(n):
    for i in range(n):
        print(i)

    for i in range(n):
        print(i)

twoLoops(3)