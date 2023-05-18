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

def mostrar(l):
    for i in range(len(l)):
        print(l[i])


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
    l[0][0] = 2 #a11
    l[1][2] = 3 #a23
    l[2][1] = 1 #a32
    l[1][1] = centro(3) #a22
    l[0][1] = c_m(3) - (l[1][1] + l[2][1]) #a12
    l[0][2] = c_m(3) - (l[0][0] + l[0][1]) #a13
    l[2][2] = c_m(3) - (l[0][2] + l[1][2]) #a33
    l[2][0] = c_m(3) - (l[2][1] + l[2][2]) #a31
    l[1][0] = c_m(3) - (l[2][0] + l[0][0]) #a21

    verificacao(l, 3)

    print (l[0])
    print (l[1])
    print (l[2])

def matriz(n):
    l=[]

    for i in range(n):
        k=[] 
        for j in range(n):
            k.append(0)
        l.append(k)

    m = int((n+1)/2)
    y = int(((n**2+1)/2) + ((n - 1)/2))
    x = int((n**2+1)/2)
    p = n - 1
    p2 = m - 1
    sm = s_m(n)

    l[0][0] = 2 
    l[p2][p] = 3 
    l[p][p2] = 1
    l[p2][p2] = x
    l[0][1] = sm - y
    l[0][p2] = int(n**2)
    l[0][p-1] = y + 2
    l[0][p] = x + 1 - m
    l[1][1] = l[0][0] + n

    mostrar(l)

#matriz_1()
#matriz_3()
matriz(5)
print()
matriz(7)