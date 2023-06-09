import time

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
    time.sleep(0.43)
    for i in range(len(l)):
        print(l[i])
    print()


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
    mostrar(l)
    l[1][2] = 3 #a23
    mostrar(l)
    l[2][1] = 1 #a32
    mostrar(l)
    l[1][1] = centro(3) #a22
    mostrar(l)
    l[0][1] = c_m(3) - (l[1][1] + l[2][1]) #a12
    mostrar(l)
    l[0][2] = c_m(3) - (l[0][0] + l[0][1]) #a13
    mostrar(l)
    l[2][2] = c_m(3) - (l[0][2] + l[1][2]) #a33
    mostrar(l)
    l[2][0] = c_m(3) - (l[2][1] + l[2][2]) #a31
    mostrar(l)
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
            k.append('')
        l.append(k)

    m = int((n+1)/2)
    y = int(((n**2+1)/2) + ((n - 1)/2))
    x = int((n**2+1)/2)
    p = n - 1
    p2 = m - 1
    sm = s_m(n)

    l[0][0] = 2 
    mostrar(l)
    l[p2][p] = 3 
    mostrar(l)
    l[p][p2] = 1
    mostrar(l)
    l[p2][p2] = x
    mostrar(l)
    l[0][1] = sm - y - 1
    mostrar(l)
    l[0][p2] = int(n**2)
    mostrar(l)
    l[0][p-1] = y + 2
    mostrar(l)
    l[1][1] = l[0][0] + n
    mostrar(l)
    l[p2][0] = int(n**2 - 2)
    mostrar(l)
    l[p][0] = y
    mostrar(l)
    l[p][1] = y + 1
    mostrar(l)
    l[p][p] = int(n**2 - 1)
    mostrar(l)
    
    c = m
    for i in range(p):
        c = c - 1
        l[i][p-i] = x - c
        mostrar(l)

    for i in range(2, p2):
        l[0][i] = l[0][i-1] - 2
        mostrar(l)

    for i in range(p-2, p2, -1):
        l[0][i] = l[0][i+1] + 2
        mostrar(l)
    
    for i in range(1, p2):
        l[i][0] = l[i - 1][0] + 2
        l[i][p2] = l[i-1][p2] - n
        mostrar(l)

    c = n - 3
    c2 = 0
    for i in range(p2+1,p):
        l[i][0] = l[p2][0] - c + c2
        c2 += 2
        mostrar(l)
    
    for i in range(p-1, p2, -1):
        l[i][p2] = l[i+1][p2] + n
        mostrar(l)

    l[1][p] = sm - l[1][0]
    mostrar(l)

    for i in range(2, p2):
        l[i][p] = l[i-1][p] - 2
        mostrar(l)

    l[p2+1][p] = sm - l[p2+1][0]
    mostrar(l)

    for i in range(p2+2, p):
        l[i][p] = l[i-1][p] - 2
        mostrar(l)

    l[p][p2+1] = sm - l[0][p2+1]
    mostrar(l)

    for i in range(p2+2,p):
        l[p][i] = l[p][i-1] + 2
        mostrar(l)

    for i in range(2, p2):
        l[p][i] = l[p][i-1] + 2
        mostrar(l)

    for i in range(1, p2):
        l[p2][i] = l[p2][i-1] - n
        mostrar(l)

    for i in range(p-1, p2, -1):
        l[p2][i] = l[p2][i+1] + n
        mostrar(l)

    for i in range(2, p2):
        l[i][i] = l[i-1][i-1] + n
        mostrar(l)

    for i in range(p-1, p2, -1):
        l[i][i] = l[i+1][i+1] - n
        mostrar(l)

    if n > 5:
        l[1][p-2] = l[p2][p-1] + 2
        mostrar(l)
        l[p-1][p-2] = sm - l[1][p-2]
        mostrar(l)
        l[p-1][2] = l[p2][p-1] + 1
        mostrar(l)
        l[1][2] = sm - l[p-1][2]
        mostrar(l)
        

    mostrar(l)

#matriz_1()
#matriz_3()
#matriz(5)
print()
#matriz(7)
print()
#matriz(9)
n = int(input('n: '))
if n == 1:
    matriz_1()
elif n == 3:
    matriz_3()
else:
    matriz(n)