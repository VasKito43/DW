def criador(n):
    v = '  '
    x = []
    l=[]
    for i in range (n):
       x.append(v) 

    for i in range (n):
        l.append(x)

    return l

def criador2(l):
    m = []
    for i in range(1, len(l)+1):
        m.append(i)
    print(m)
    


    print(l)

def mostrar(l):
    for i in range(len(l)):
        print(l[i])
    print()

criador2(criador(3))