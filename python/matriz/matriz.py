def centro(n):
    n = (n**2 + 1)/2
    return int(n)

def somar_termos(a):
    s = 0
    for i in a:
        for j in i:
            s += j
    return s

def verificacao(l,n):
    cm = c_m(n)
    for i in range (len(l)):
        soma = 0
        for j in range (len(l)):
            soma += l[i][j]
        if soma != cm:
            print('!!falha!!')
    for i in range (len(l)):
        soma = 0
        for j in range (len(l)):
            soma += l[j][i]
        if soma != cm:
            print('!!falha!!')


def s_t(n):
    s = ((n**2 + 1)/2) * (n**2)
    return int(s)

def c_m(n):
    c = ((n**2 + 1)/2) * n
    return int(c)

def s_m(n):
    s = n**2 + 1
    return int(s)

def matriz_1():
    l = [[1]]
    st = somar_termos(l)
    if st == s_t(1) and c_m(1) == 1:
        print (l)

def matriz_3():
    l = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    sm = s_m(3)
    l[0][0] = 2
    l[1][2] = 3
    l[2][1] = 1
    l[1][1] = centro(3)
    l[0][1] = c_m(3) - (l[1][1] + l[2][1])
    l[0][2] = c_m(3) - (l[0][0] + l[0][1])
    l[2][2] = c_m(3) - (l[0][2] + l[1][2])
    l[2][0] = c_m(3) - (l[2][1] + l[2][2])
    l[1][0] = c_m(3) - (l[2][0] + l[0][0])

    verificacao(l, 3)

    print (l[0])
    print (l[1])
    print (l[2])

matriz_1()
matriz_3()