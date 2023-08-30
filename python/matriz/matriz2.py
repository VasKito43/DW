import time

def criador(n): #criador da matriz
    l=[]

    for i in range(n):
        k=[] 
        for j in range(n):
            k.append(' ')
        l.append(k)

    return l

def criador2(n): #criador da lista de conferencia
    m = [];
    x = [];
    for i in range(1, n**2+1):
        m.append(i)
        if i % n == 0:
            x.append(m)
            m = []
    return x

def contador(l): #soma todos os elemntos da lista
    soma = 0
    for i in range(len(l)):
        for j in range(len(l)):
            soma += l[i][j]
    return soma

def menor(l): #acha o menor valor da lista
    menor = 999999999999999999*9999
    for i in range(len(l)):
        for j in range(len(l)):
            if menor > l[i][j] and l[i][j] != 0:
                menor = l[i][j]
    return menor

def diagonal(v):
    c = False
    global n, m
    for i in range(n):
        if m[i][i] == v:
            c = True
    w = y
    for i in range(n):
        if m[w][i] == v:
            c = True
        w -= 1
    return c
        

def verificador(l): #verifica se as colunas e linhas tem o valor de C.M
    v = 0
    for i in range(len(l)):
        somar = 0
        for j in range(len(l)):
            somar += l[j][i]
        print(somar)
        if somar != cm:
            v = 1
    for i in range(len(l)):
        somar = 0
        for j in range(len(l)):
            somar += l[i][j]
        print(somar)
        if somar != cm:
            v = 1

    somar = 0
    for i in range(len(l)):
        for j in range(len(l)):
            somar += l[j][i]
            
    if somar != st:
        v = 1

    if v == 1:
        print('!!ERRO!!')
    else:
        print('Matriz Perfeita')

    
def mostrar(l): #visualizaçao da matriz
    time.sleep(0.45)
    for i in range(len(l)):
        print(l[i])
    print()

def removedor(v): #remove valor da lista de conferencia
    global l
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i][j] == v:
                l[i][j] = 0

n = 14#int(input('n: '))
m = criador(n) #matriz
l = criador2(n) #lista de conferencia
x = int((n+1)/2) - 1 #localização da metade da matriz
y = n-1 # localização de 'n' na lista
sm = int(n**2 + 1) #S.M
cm = int(((n**2 + 1)/2)*n) #C.M
st = int(((n**2+1)/2)*(n**2)) #S.T

if n % 2 == 0:

    n1 = n + 1
    n2 = n - 1
    x1 = int(n/2-1)
    x2 = int(n/2)

    #valores fixos

    m[0][0] = 1
    m[y][0] = n
    m[0][y-1] = n + 1

    w = y
    for i in range (n-1): #primeira diagonal 
        m[i+1][i+1] = m[i][i] + n1
        m[w-1][i+1] = m[w][i] + n2
        w -= 1

    #sequencia 1

    for i in range (x1):
        m[i+1][0] = m[i][0] + 1
        m[i+1][y] = m[i][y] + 1
    
    m[x1][y] = m[x1-1][0] + 1
    m[x1][0] = m[x1-1][y] + 1

    for i in range(x1, n-2):
        m[i+1][y] = m[i][y] + 1
        m[i+1][0] = m[i][0] + 1


    #linha 1

    m[0][1] = m[0][y] - 1


    for i in range(1, x2):
        m[0][i+1] = m[0][i] - n


    for i in range(y-1, x2+1, -1):
        m[0][i-1] = m[0][i] + n


    #ultima linha 

    m[y][x1] = sm - m[0][x2]
    m[y][x2] = sm - m[0][x1]

    w = x2 + 1
    for i in range(x1, 1, -1):
        m[y][i-1] = m[y][i] + n
        m[y][w] = sm - m[y][i-1]
        w += 1

    #coluna central 

    for i in range(y, x2+1, -1):
        m[i-1][x1] = m[i][x1] + 1
        m[i-1][x2] = m[i][x2] + 1

    m[1][x2] = m[0][x1] - 1
    m[1][x1] = m[0][x2] - 1

    for i in range(1, x1-1):
        m[i+1][x1] = m[i][x1]-1
        m[i+1][x2] = m[i][x2]-1


    #preenchimento
    w = y - 1
    for l in range(1,x1-1):
        for i in range(x1-1, 0, -1):
            if diagonal(m[l][i]) or diagonal(m[w][i]):
                break
            else:
                m[l][i] = m[l][i+1] - n
                m[w][i] = m[w][i+1] + n
        w -= 1
    w = y - 1
    for l in range(1,x1-1):
        for i in range(x2+1, y):
            if diagonal(m[l][i]) or diagonal(m[w][i]):
                break
            else:
                m[l][i] = m[l][i-1] + n
                m[w][i] = m[w][i-1] - n
        w -= 1

    for l in range(1,x1):
        m[(l-2*l)-2][(l-2*l)-1] = m[l][l] + 1

    w = 1
    for l in range(y-1, x2, -1):
        m[(w-2*w)-2][(l-2*l)-1] = m[w][l] + 1
        w += 1
        
    for l in range(1, y):
        for i in range(y-1, x1+1, -1):
            if m[i-1][l] == ' ':
                m[i-1][l] = m[i][l] + 1

    for l in range(y, x1, -1):
        for i in range(1, y):
            if diagonal(m[l][i]) and m[(l-2*l)][i] == ' ':
                m[(l-2*l)][i] = m[l][i] - 1
                
    for l in range(1, x1):
        for i in range(1, y):
            if diagonal(m[l][i]) and m[l+2][i] == ' ':
                for k in range(l+1, x1):
                    m[k+1][i] = m[k][i] - 1
    

    mostrar(m)
else:
    z = int((n**2 + 1)/2) 

    #valores fixos

    m[0][0] = 2
    mostrar (m)
    m[x][x] = z
    mostrar (m)
    m[x][y] = 3
    mostrar (m)
    m[y][x] = 1
    mostrar (m)
    m[0][x] = sm - 1
    mostrar (m)
    m[y][y] = sm - 2
    mostrar (m)
    m[x][0] = sm - 3
    mostrar (m)

    removedor(m[0][0])
    removedor(m[x][x])
    removedor(m[x][y])
    removedor(m[y][x])
    removedor(m[0][x])
    removedor(m[y][y])
    removedor(m[x][0])


    c = int((n+1)/2)
    p = n - 1
    for i in range(n): #primeira diagonal
        c = c - 1
        m[i][p-i] = z - c
        mostrar (m)
        removedor(m[i][p-i])

    for i in range(x-1): #segunda diagonal
        m[i+1][i+1] = m[i][i] + n
        mostrar (m)
        removedor(m[i+1][i+1])

    for i in range(y, x+1, -1): #segunda diagonal
        m[i-1][i-1] = m[i][i] - n
        mostrar (m)
        removedor(m[i-1][i-1])

    for i in range(x-1): #coluna central
        m[i+1][x] = m[i][x] - n
        mostrar (m)
        removedor(m[i+1][x])

    for i in range(y, x+1, -1): #coluna central
        m[i-1][x] = m[i][x] + n
        mostrar (m)
        removedor(m[i-1][x])

    for i in range(x-1): #linha central
        m[x][i+1] = m[x][i] - n
        mostrar (m)
        removedor(m[x][i+1])

    for i in range(y, x+1, -1): #linha central
        m[x][i-1] = m[x][i] + n
        mostrar (m)
        removedor(m[x][i-1])

    #ordem crescente    
    w=0
    l1 = y
    l2 = 0
    while contador(l) > 0:

        while True:
            a = 0

            for j in range(x):
                if m[l1][j] == ' ':
                    m[l1][j] = menor(l)
                    mostrar (m)
                    m[l2][j] = sm - m[l1][j]
                    mostrar (m)
                    removedor(m[l1][j])
                    removedor(m[l2][j])
                    break

            for j in range(y, x, -1):
                if m[l2][j] == ' ':
                    m[l2][j] = menor(l)
                    mostrar (m)
                    m[l1][j] = sm - m[l2][j]
                    mostrar (m)
                    removedor(m[l2][j])
                    removedor(m[l1][j])
                    a += 1
                    break

            if a == 0:
                break
            
        while True:
            a = 0

            for j in range(x):
                if m[j][l2] == ' ':
                    m[j][l2] = menor(l)
                    mostrar (m)
                    m[j][l1] = sm - m[j][l2]
                    mostrar (m)
                    removedor(m[j][l2])
                    removedor(m[j][l1])
                    break

            for j in range(y, x, -1):
                if m[j][l1] == ' ':
                    m[j][l1] = menor(l)
                    mostrar (m)
                    m[j][l2] = sm - m[j][l1]
                    mostrar (m)
                    removedor(m[j][l1])
                    removedor(m[j][l2])
                    a += 1
                    break

            if a == 0:
                break
            
            
        l1 -= 1 
        l2 += 1



verificador(m)
