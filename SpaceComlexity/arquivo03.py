#Nesta primeira função temos O(a + b), pois temos duas variaveis que podem ter o mesmo valor ou valores diferentes,
#fazendo assim com que seja necessário somar as duas variáveis. Neste exemplo teremos 5 saidas.

def twoInputsAdd(a, b):
    for i in range(a):
        print(i)

    for i in range(b):
        print(i)


#Nesta situação temos O(a * b), pois temos as variaveis diferentes. Neste exemplo teremos seis saidas
def twoInputsMult(a, b):
    for i in range(a):
        for j in range(b):
            print(a, b)


twoInputsAdd(2, 3)
twoInputsMult(2, 3)