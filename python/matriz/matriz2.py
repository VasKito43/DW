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
    menor = 999999999999999999
    for i in range(len(l)):
        for j in range(len(l)):
            if menor > l[i][j] and l[i][j] != 0:
                menor = l[i][j]
    return menor

def verificador(l): #verifica se as colunas e linhas tem o valor de C.M
    v = 0
    for i in range(len(l)):
        somar = 0
        for j in range(len(l)):
            somar += l[j][i]
        if somar != cm:
            v = 1
    for i in range(len(l)):
        somar = 0
        for j in range(len(l)):
            somar += l[i][j]
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

n = int(input('n: '))
m = criador(n) #matriz
l = criador2(n) #lista de conferencia

x = int((n+1)/2) - 1 #localização da metade da matriz
y = n-1 # localização de 'n' na lista
z = int((n**2 + 1)/2)
sm = int(n**2 + 1) #S.M
cm = int(((n**2 + 1)/2)*n) #C.M
st = int(((n**2+1)/2)*(n**2))

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
