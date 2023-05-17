def somar_termos(lista):
    s = 0
    for sublist in lista:
        for num in sublist:
            s += num
    return s

def st(n):
    s = ((n ** 2) / 2) * (n ** 2)
    return s

def cm(n):
    c = ((n ** 2) / 2) * n
    return c

def matriz_1():
    l = [[1]]  # A lista deve conter sublistas, então aqui usamos [[1]]
    st_value = somar_termos(l)
    if st_value == st(1) and cm(1) == 1:
        print(l)

matriz_1()