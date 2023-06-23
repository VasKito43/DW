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
    print(soma)

def menor(l): #acha o menor valor da lista
    menor = 999999999999999999
    for i in range(len(l)):
        for j in range(len(l)):
            if menor > l[i][j] and l[i][j] != 0:
                menor = l[i][j]
    
def mostrar(l): #visualizaçao da matriz
    for i in range(len(l)):
        print(l[i])
    print()

def removedor(v): #remove valor da lista de conferencia
    global l
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i][j] == v:
                l[i][j] = 0

n = 7#int(input('n: '))
m = criador(n) #matriz
l = criador2(n) #lista de conferencia

x = int((n+1)/2) - 1 #localização da metade da matriz
y = n-1 # localização de 'n' na lista
z = int((n**2+1)/2)
sm = int(n**2+1) #S.M


#valores fixos

m[0][0] = 2
m[x][x] = z
m[x][y] = 3
m[y][x] = 1

m[0][x] = sm - 1
m[y][y] = sm - 2
m[x][0] = sm - 3

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
    removedor(m[i][p-i])

for i in range(x-1): #segunda diagonal
    m[i+1][i+1] = m[i][i] + n
    removedor(m[i+1][i+1])

for i in range(y, x+1, -1): #segunda diagonal
    m[i-1][i-1] = m[i][i] - n
    removedor(m[i-1][i-1])

for i in range(x-1): #coluna central
    m[i+1][x] = m[i][x] - n
    removedor(m[i+1][x])

for i in range(y, x+1, -1): #coluna central
    m[i-1][x] = m[i][x] + n
    removedor(m[i-1][x])

for i in range(x-1): #linha central
    m[x][i+1] = m[x][i] - n
    removedor(m[x][i+1])

for i in range(y, x+1, -1): #linha central
    m[x][i-1] = m[x][i] + n
    removedor(m[x][i-1])

#ordem crescente    

# while contador(l) > 0:
#     for i in range(x):
#         if i == ' ':
menor(l)
mostrar(l)
mostrar (m)