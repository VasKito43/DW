def criador(n):
    v = '  '
    x = [];
    l=[];
    for i in range (n):
       x.append(v) 

    for i in range (n):
        l.append(x)

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

n = int(input('n: '))
m = criador(n)
l = criador2(n)

x = int((n+1)/2)
y = n-1

#valores fixos

m[0][0] = 2
m[x][x] = int(n**2/2)
m[x][y] = 1
m[y][x] = 3
removedor(m[0][0])
removedor(m[x][x])
removedor(m[x][y])
removedor(m[y][x])

mostrar (m)