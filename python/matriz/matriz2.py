def criador(n):
    l=[]

    for i in range(n):
        k=[] 
        for j in range(n):
            k.append(' ')
        l.append(k)

    return l

def criador2(n):
    m = [];
    x = [];
    for i in range(1, n**2+1):
        m.append(i)
        if i % n == 0:
            x.append(m)
            m = []
    return x
    

def mostrar(l):
    for i in range(len(l)):
        print(l[i])
    print()

def removedor(v):
    global l
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i][j] == v:
                l[i][j] = 0

n = 7#int(input('n: '))
m = criador(n)
l = criador2(n)

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

c = int((n+1)/2)
p = n - 1
for i in range(n): #primeira diagonal
    c = c - 1
    m[i][p-i] = z - c

for i in range(x-1): #segunda diagonal
    m[i+1][i+1] = m[i][i] + n

for i in range(y, x+1, -1): #segunda diagonal
    m[i-1][i-1] = m[i][i] - n

for i in range(x-1): #coluna central
    m[i+1][x] = m[i][x] - n

for i in range(y, x+1, -1): #coluna central
    m[i-1][x] = m[i][x] + n



mostrar (m)