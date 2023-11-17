
def criador_de_matriz_vazia(n): # criador da matriz vazia
    lista=[]

    for i in range(n):
        matriz_vazia=[] 
        for j in range(n):
            matriz_vazia.append(' ')
        lista.append(matriz_vazia)

    return lista

def criador_de_matriz_de_conferencia(n): # cria a matriz de conferencia
    matriz1 = [1]
    matriz2 = []
    for i in range(n-1):
        matriz1.append(matriz1[i]+n)
    matriz2.append(matriz1)
    matriz3 = matriz1[:]
    for i in range(n-1):
        matriz1 = matriz3[:]
        matriz3 = matriz1[:]
        for f in range(n):
            matriz3[f] += 1
        matriz2.append(matriz3)
    return matriz2

def contador(lista_de_conferencia): # soma todos os elemntos da lista
    soma = 0
    for linha in range(len(lista_de_conferencia)):
        for coluna in range(len(lista_de_conferencia)):
            soma += lista_de_conferencia[linha][coluna]
    return soma

def menor(lista_de_conferencia): # acha o menor valor da lista
    menor = 999999999999999999*9999
    for i in range(len(lista_de_conferencia)):
        for j in range(len(lista_de_conferencia)):
            if menor > lista_de_conferencia[i][j] and lista_de_conferencia[i][j] != 0:
                menor = lista_de_conferencia[i][j]
    return menor

def diagonal(valor, n, matriz, n_na_matriz): # identifica se o valor da matriz é uma diagonal
    verificar = False
    for i in range(n):
        if matriz[i][i] == valor:
            verificar = True
    variavel = n_na_matriz
    for i in range(n):
        if matriz[variavel][i] == valor:
            verificar = True
        variavel -= 1
    return verificar
        
def verificador(lista_de_conferencia, cm, st): # verifica se as colunas e linhas tem o valor de C.matriz
    verifica = 0
    for i in range(len(lista_de_conferencia)):
        somar = 0
        for j in range(len(lista_de_conferencia)):
            somar += lista_de_conferencia[j][i]
        if somar != cm:
            verifica = 1

    for i in range(len(lista_de_conferencia)):
        somar = 0
        for j in range(len(lista_de_conferencia)):
            somar += lista_de_conferencia[i][j]
        if somar != cm:
            verifica = 1

    somar = 0
    for i in range(len(lista_de_conferencia)):
        for j in range(len(lista_de_conferencia)):
            somar += lista_de_conferencia[j][i]
            
    if somar != st:
        verifica = 1

    if verifica == 1:
        print('!!ERRO!!')
    else:
        print('Quadrado Perfeito')
    


def removedor(valor, lista_de_conferencia): # remove valor da lista de conferencia
    for i in range(len(lista_de_conferencia)):
        for j in range(len(lista_de_conferencia)):
            if lista_de_conferencia[i][j] == valor:
                lista_de_conferencia[i][j] = 0
