import time

def criador(n): # criador da matriz vazia
    l=[]

    for i in range(n):
        k=[] 
        for j in range(n):
            k.append(' ')
        l.append(k)

    return l

def criador2(n): # cria a matriz de conferencia
    m = [1]
    x = []
    for i in range(n-1):
        m.append(m[i]+n)
    x.append(m)
    z = m[:]
    for i in range(n-1):
        m = z[:]
        z = m[:]
        for f in range(n):
            z[f] += 1
        x.append(z)
    return x

def contador(l): # soma todos os elemntos da lista
    soma = 0
    for i in range(len(l)):
        for j in range(len(l)):
            soma += l[i][j]
    return soma

def menor(l): # acha o menor valor da lista
    menor = 999999999999999999*9999
    for i in range(len(l)):
        for j in range(len(l)):
            if menor > l[i][j] and l[i][j] != 0:
                menor = l[i][j]
    return menor

def diagonal(v): # identifica se o valor da matriz é uma diagonal
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
        

def verificador(l): # verifica se as colunas e linhas tem o valor de C.M
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

    
def mostrar(l): # visualizaçao da matriz
    global n
    time.sleep(4/n)
    for i in range(len(l)):
        print(l[i])
    print()

def removedor(v): # remove valor da lista de conferencia
    global l
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i][j] == v:
                l[i][j] = 0

n = int(input('Digite o valor de n para a matriz: '))
m = criador(n) # criar matriz
l = criador2(n) # criar lista de conferencia
x = int((n+1)/2) - 1 # localização da metade da matriz
y = n-1 # localização de 'n' na matriz
sm = int(n**2 + 1) # Soma Magica
cm = int(((n**2 + 1)/2)*n) # Constante Magica
st = int(((n**2+1)/2)*(n**2)) # Soma de Termos

print()
if n <= 2:
    print('matriz impossivel')

elif n % 2 == 0:
    
    # valores fixos
    m[0][0] = 1
    m[y][0] = n
    m[y][y] = n**2
    print('valores fixos')
    print()
    mostrar (m)

    w = y

    for i in range(y): # diagonais
        m[i+1][i+1] = m[i][i] + n + 1
        m[w-1][i+1] = m[w][i] + n - 1
        w -= 1
    print('diagonais')
    print()
    mostrar (m)
    
    if n % 4 == 0: # Matriz de ordem par com modulo 4 = 0

        for f in range(x+1): # preenchimento
            if f % 2 == 0: 
                for i in range(0, y+1):
                    if not diagonal(l[i][f]): 
                        if (l[i][f] % 2 == 0 and i <= x) or (l[i][f] % 2 != 0 and i > x):
                            m[y-i][y-f] = l[i][f]
                        elif (l[i][f] % 2 != 0 and i <= x) or (l[i][f] % 2 == 0 and i > x): 
                            m[i][f] = l[i][f]
                        if (l[i][y-f] % 2 == 0 and i <= x) or (l[i][y-f] % 2 != 0 and i > x):
                            m[y-i][f] = l[i][y-f]
                        elif (l[i][y-f] % 2 != 0 and i <= x) or (l[i][y-f] % 2 == 0 and i > x): 
                            m[i][y-f] = l[i][y-f]

            else:
                for i in range(0, y+1):
                    if not diagonal(l[i][f]):
                        if (l[i][f] % 2 != 0 and i <= x) or (l[i][f] % 2 == 0 and i > x):
                            m[y-i][y-f] = l[i][f]
                        elif (l[i][f] % 2 == 0 and i <= x) or (l[i][f] % 2 != 0 and i > x): 
                            m[i][f] = l[i][f]
                        if (l[i][y-f] % 2 != 0 and i <= x) or (l[i][y-f] % 2 == 0 and i > x):
                            m[y-i][f] = l[i][y-f]
                        elif (l[i][y-f] % 2 == 0 and i <= x) or (l[i][y-f] % 2 != 0 and i > x): 
                            m[i][y-f] = l[i][y-f]


    else: # Matriz de ordem par com modulo 4 = 2
        m[x][y] = l[x][0]
        m[x+1][y] = l[x+1][0]

        m[x][0] = sm - m[x][y]
        m[x+1][0] = sm - m[x+1][y]

        m[y][x] = l[0][x]
        m[y][x+1] = l[0][x+1]
        m[0][x] = sm - m[y][x]
        m[0][x+1] = sm - m[y][x+1]

        for i in range(1,x): # colunas centrais
            if i % 2 == 0:
                m[x][y-i] = l[x][i]
                m[x+1][y-i] = l[x+1][i]
                m[x+1][i] = sm - m[x][y-i]
                m[x][i] = sm - m[x+1][y-i]

                m[y-i][x] = l[i][x]
                m[y-i][x+1] = l[i][x+1]
                m[i][x+1] = sm - m[y-i][x]
                m[i][x] = sm - m[y-i][x+1]
            else:
                m[x+1][i] = l[x][y-i]
                m[x+1][y-i] = l[x][i]
                m[x][i] = sm - m[x+1][i]
                m[x][y-i] = sm - m[x+1][y-i]

                m[y-i][x] = l[y-i][x+1]
                m[y-i][x+1] = sm - m[y-i][x]
                m[i][x+1] = l[y-i][x]
                m[i][x] = sm - m[i][x+1]
        print('colunas')
        print()
        mostrar (m)

        for f in range(x): # preenchimento
            for i in range(x):
                if diagonal(m[i][f]):
                    for g in range(f+1,x):
                        if (l[y-g][f] % 2 != 0 and f % 2 == 0) or (l[y-g][f] % 2 == 0 and f % 2 != 0):
                            m[g][f] = l[y-g][f]
                            m[g][y-f] = l[y-g][y-f]
                            m[y-g][y-f] = l[g][f]
                            m[y-g][f] = l[g][y-f]

                            m[f][g] = l[f][y-g]
                            m[y-f][g] = l[y-f][y-g]
                            m[y-f][y-g] = l[f][g]
                            m[f][y-g] = l[y-f][g]
                        else:
                            m[g][f] = l[g][f]
                            m[g][y-f] = l[g][y-f]
                            m[y-g][y-f] = l[y-g][f]
                            m[y-g][f] = l[y-g][y-f]

                            m[f][g] = l[f][g]
                            m[y-f][g] = l[y-f][g]
                            m[y-f][y-g] = l[f][y-g]
                            m[f][y-g] = l[y-f][y-g]

                        
    print('preenchimento')
    print()
    mostrar(m)
    verificador(m)
else: #valores impares
    z = int((n**2 + 1)/2) 

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

    print('valores fixos')
    print()
    mostrar (m)


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
    print('diagonal')
    print()
    mostrar (m)

    for i in range(x-1): #coluna central
        m[i+1][x] = m[i][x] - n
        removedor(m[i+1][x])

    for i in range(y, x+1, -1): #coluna central
        m[i-1][x] = m[i][x] + n
        removedor(m[i-1][x])

    print('coluna central')
    print()
    mostrar (m)

    for i in range(x-1): #linha central
        m[x][i+1] = m[x][i] - n
        removedor(m[x][i+1])

    for i in range(y, x+1, -1): #linha central
        m[x][i-1] = m[x][i] + n
        removedor(m[x][i-1])
    
    print('linha central')
    print()
    mostrar (m)

    #ordem crescente    
    w=0
    l1 = y
    l2 = 0
    while contador(l) > 0:

            
        while True:
            a = 0

            for j in range(x):
                if m[j][l2] == ' ':
                    m[j][l2] = menor(l)
                    m[j][l1] = sm - m[j][l2]
                    removedor(m[j][l2])
                    removedor(m[j][l1])
                    break

            for j in range(y, x, -1):
                if m[j][l1] == ' ':
                    m[j][l1] = menor(l)
                    m[j][l2] = sm - m[j][l1]
                    removedor(m[j][l1])
                    removedor(m[j][l2])
                    a += 1
                    break

            if a == 0:
                break
            
        while True:
            a = 0

            for j in range(x):
                if m[l1][j] == ' ':
                    m[l1][j] = menor(l)
                    m[l2][j] = sm - m[l1][j]
                    removedor(m[l1][j])
                    removedor(m[l2][j])
                    break

            for j in range(y, x, -1):
                if m[l2][j] == ' ':
                    m[l2][j] = menor(l)
                    m[l1][j] = sm - m[l2][j]
                    removedor(m[l2][j])
                    removedor(m[l1][j])
                    a += 1
                    break

            if a == 0:
                break
            
        l1 -= 1 
        l2 += 1
    print('preenchimento')
    print()
    mostrar(m)
    verificador(m)


