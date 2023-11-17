import time

from tkinter import *

def criar_tabela(matriz, quadrado):
    global num
    tabela = []  # Lista para armazenar os widgets Entry

    for i in range(num):
        linha = []
        for j in range(num):
            entry = Entry(janela, width=5)
            entry.insert(0, matriz[i][j])  # Insere o valor na célula
            entry.grid(row=i+3+(num*(quadrado-1))+(quadrado-1), column=j, padx=5, pady=5)
            # linha.append(entry)
        # tabela.append(linha)

    return tabela  # Retorna a tabela criada

def coletar_entrada():
    valor = int(valor_n.get())
    return valor

def criador(n): # criador da matriz vazia
    lista=[]

    for i in range(n):
        variavel=[] 
        for j in range(n):
            variavel.append(' ')
        lista.append(variavel)

    return lista

def criador2(n): # cria a matriz de conferencia
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
    for i in range(len(lista_de_conferencia)):
        for j in range(len(lista_de_conferencia)):
            soma += lista_de_conferencia[i][j]
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
        texto_verificacao['text'] = '!!ERRO!!'
    else:
        texto_verificacao['text'] = 'Quadrado Perfeito'
    
def mostrar(texto, quadrado, matriz): # visualizaçao da matriz
    
    if quadrado == 1:
        texto_quadrado1['text'] = texto
        matriz_quadrado1['text'] = criar_tabela(matriz, quadrado)

    elif quadrado == 2:
        texto_quadrado2['text'] = texto
        matriz_quadrado2['text'] = criar_tabela(matriz, quadrado)

    elif quadrado == 3:
        texto_quadrado3['text'] = texto
        matriz_quadrado3['text'] = criar_tabela(matriz, quadrado)

    elif quadrado == 4:
        texto_quadrado4['text'] = texto
        matriz_quadrado4['text'] = criar_tabela(matriz, quadrado)

    elif quadrado == 5:
        texto_quadrado5['text'] = texto
        matriz_quadrado5['text'] = criar_tabela(matriz, quadrado)

def removedor(valor, lista_de_conferencia): # remove valor da lista de conferencia
    for i in range(len(lista_de_conferencia)):
        for j in range(len(lista_de_conferencia)):
            if lista_de_conferencia[i][j] == valor:
                lista_de_conferencia[i][j] = 0

quadrado = ''
num = 5

def algoritmo():
    global quadrado
    global num
    n = coletar_entrada()#int(input('Digite o valor de n para a matriz: '))
    matriz = criador(n) # criar matriz
    lista_de_conferencia = criador2(n) # criar lista de conferencia
    metade_matriz = int((n+1)/2) - 1 # localização da metade da matriz
    n_na_matriz = n-1 # localização de 'n' na matriz
    sm = int(n**2 + 1) # Soma Magica
    cm = int(((n**2 + 1)/2)*n) # Constante Magica
    st = int(((n**2+1)/2)*(n**2)) # Soma de Termos

    num = n

    if n <= 2:
        mostrar('matriz imposivel', 1, matriz)

    elif n % 2 == 0:

        # valores fixos
        matriz[0][0] = 1
        matriz[n_na_matriz][0] = n
        matriz[n_na_matriz][n_na_matriz] = n**2
        mostrar('valores fixos', 1, matriz)

        w = n_na_matriz

        for i in range(n_na_matriz): # diagonais
            matriz[i+1][i+1] = matriz[i][i] + n + 1
            matriz[w-1][i+1] = matriz[w][i] + n - 1
            w -= 1
        mostrar('diagonais', 2, matriz)

        if n % 4 == 0: # Matriz de ordem par com modulo 4 = 0

            for f in range(metade_matriz+1): # preenchimento
                if f % 2 == 0: 
                    for i in range(0, n_na_matriz+1):
                        if not diagonal(lista_de_conferencia[i][f], n, matriz, n_na_matriz): 
                            if (lista_de_conferencia[i][f] % 2 == 0 and i <= metade_matriz) or (lista_de_conferencia[i][f] % 2 != 0 and i > metade_matriz):
                                matriz[n_na_matriz-i][n_na_matriz-f] = lista_de_conferencia[i][f]
                            elif (lista_de_conferencia[i][f] % 2 != 0 and i <= metade_matriz) or (lista_de_conferencia[i][f] % 2 == 0 and i > metade_matriz): 
                                matriz[i][f] = lista_de_conferencia[i][f]
                            if (lista_de_conferencia[i][n_na_matriz-f] % 2 == 0 and i <= metade_matriz) or (lista_de_conferencia[i][n_na_matriz-f] % 2 != 0 and i > metade_matriz):
                                matriz[n_na_matriz-i][f] = lista_de_conferencia[i][n_na_matriz-f]
                            elif (lista_de_conferencia[i][n_na_matriz-f] % 2 != 0 and i <= metade_matriz) or (lista_de_conferencia[i][n_na_matriz-f] % 2 == 0 and i > metade_matriz): 
                                matriz[i][n_na_matriz-f] = lista_de_conferencia[i][n_na_matriz-f]

                else:
                    for i in range(0, n_na_matriz+1):
                        if not diagonal(lista_de_conferencia[i][f], n, matriz, n_na_matriz):
                            if (lista_de_conferencia[i][f] % 2 != 0 and i <= metade_matriz) or (lista_de_conferencia[i][f] % 2 == 0 and i > metade_matriz):
                                matriz[n_na_matriz-i][n_na_matriz-f] = lista_de_conferencia[i][f]
                            elif (lista_de_conferencia[i][f] % 2 == 0 and i <= metade_matriz) or (lista_de_conferencia[i][f] % 2 != 0 and i > metade_matriz): 
                                matriz[i][f] = lista_de_conferencia[i][f]
                            if (lista_de_conferencia[i][n_na_matriz-f] % 2 != 0 and i <= metade_matriz) or (lista_de_conferencia[i][n_na_matriz-f] % 2 == 0 and i > metade_matriz):
                                matriz[n_na_matriz-i][f] = lista_de_conferencia[i][n_na_matriz-f]
                            elif (lista_de_conferencia[i][n_na_matriz-f] % 2 == 0 and i <= metade_matriz) or (lista_de_conferencia[i][n_na_matriz-f] % 2 != 0 and i > metade_matriz): 
                                matriz[i][n_na_matriz-f] = lista_de_conferencia[i][n_na_matriz-f]
            mostrar('preenchimento', 3, matriz)


        else: # Matriz de ordem par com modulo 4 = 2
            matriz[metade_matriz][n_na_matriz] = lista_de_conferencia[metade_matriz][0]
            matriz[metade_matriz+1][n_na_matriz] = lista_de_conferencia[metade_matriz+1][0]

            matriz[metade_matriz][0] = sm - matriz[metade_matriz][n_na_matriz]
            matriz[metade_matriz+1][0] = sm - matriz[metade_matriz+1][n_na_matriz]

            matriz[n_na_matriz][metade_matriz] = lista_de_conferencia[0][metade_matriz]
            matriz[n_na_matriz][metade_matriz+1] = lista_de_conferencia[0][metade_matriz+1]
            matriz[0][metade_matriz] = sm - matriz[n_na_matriz][metade_matriz]
            matriz[0][metade_matriz+1] = sm - matriz[n_na_matriz][metade_matriz+1]

            for i in range(1,metade_matriz): # colunas centrais
                if i % 2 == 0:
                    matriz[metade_matriz][n_na_matriz-i] = lista_de_conferencia[metade_matriz][i]
                    matriz[metade_matriz+1][n_na_matriz-i] = lista_de_conferencia[metade_matriz+1][i]
                    matriz[metade_matriz+1][i] = sm - matriz[metade_matriz][n_na_matriz-i]
                    matriz[metade_matriz][i] = sm - matriz[metade_matriz+1][n_na_matriz-i]

                    matriz[n_na_matriz-i][metade_matriz] = lista_de_conferencia[i][metade_matriz]
                    matriz[n_na_matriz-i][metade_matriz+1] = lista_de_conferencia[i][metade_matriz+1]
                    matriz[i][metade_matriz+1] = sm - matriz[n_na_matriz-i][metade_matriz]
                    matriz[i][metade_matriz] = sm - matriz[n_na_matriz-i][metade_matriz+1]
                else:
                    matriz[metade_matriz+1][i] = lista_de_conferencia[metade_matriz][n_na_matriz-i]
                    matriz[metade_matriz+1][n_na_matriz-i] = lista_de_conferencia[metade_matriz][i]
                    matriz[metade_matriz][i] = sm - matriz[metade_matriz+1][i]
                    matriz[metade_matriz][n_na_matriz-i] = sm - matriz[metade_matriz+1][n_na_matriz-i]

                    matriz[n_na_matriz-i][metade_matriz] = lista_de_conferencia[n_na_matriz-i][metade_matriz+1]
                    matriz[n_na_matriz-i][metade_matriz+1] = sm - matriz[n_na_matriz-i][metade_matriz]
                    matriz[i][metade_matriz+1] = lista_de_conferencia[n_na_matriz-i][metade_matriz]
                    matriz[i][metade_matriz] = sm - matriz[i][metade_matriz+1]
            
            mostrar('colunas', 3, matriz)

            for f in range(metade_matriz): # preenchimento
                for i in range(metade_matriz):
                    if diagonal(matriz[i][f], n, matriz, n_na_matriz):
                        for g in range(f+1,metade_matriz):
                            if (lista_de_conferencia[n_na_matriz-g][f] % 2 != 0 and f % 2 == 0) or (lista_de_conferencia[n_na_matriz-g][f] % 2 == 0 and f % 2 != 0):
                                matriz[g][f] = lista_de_conferencia[n_na_matriz-g][f]
                                matriz[g][n_na_matriz-f] = lista_de_conferencia[n_na_matriz-g][n_na_matriz-f]
                                matriz[n_na_matriz-g][n_na_matriz-f] = lista_de_conferencia[g][f]
                                matriz[n_na_matriz-g][f] = lista_de_conferencia[g][n_na_matriz-f]

                                matriz[f][g] = lista_de_conferencia[f][n_na_matriz-g]
                                matriz[n_na_matriz-f][g] = lista_de_conferencia[n_na_matriz-f][n_na_matriz-g]
                                matriz[n_na_matriz-f][n_na_matriz-g] = lista_de_conferencia[f][g]
                                matriz[f][n_na_matriz-g] = lista_de_conferencia[n_na_matriz-f][g]
                            else:
                                matriz[g][f] = lista_de_conferencia[g][f]
                                matriz[g][n_na_matriz-f] = lista_de_conferencia[g][n_na_matriz-f]
                                matriz[n_na_matriz-g][n_na_matriz-f] = lista_de_conferencia[n_na_matriz-g][f]
                                matriz[n_na_matriz-g][f] = lista_de_conferencia[n_na_matriz-g][n_na_matriz-f]

                                matriz[f][g] = lista_de_conferencia[f][g]
                                matriz[n_na_matriz-f][g] = lista_de_conferencia[n_na_matriz-f][g]
                                matriz[n_na_matriz-f][n_na_matriz-g] = lista_de_conferencia[f][n_na_matriz-g]
                                matriz[f][n_na_matriz-g] = lista_de_conferencia[n_na_matriz-f][n_na_matriz-g]


        
            mostrar('preenchimento', 4, matriz)
        verificador(matriz, cm, st)
    else: #valores impares
        z = int((n**2 + 1)/2) 

        #valores fixos

        matriz[0][0] = 2
        matriz[metade_matriz][metade_matriz] = z
        matriz[metade_matriz][n_na_matriz] = 3
        matriz[n_na_matriz][metade_matriz] = 1
        matriz[0][metade_matriz] = sm - 1
        matriz[n_na_matriz][n_na_matriz] = sm - 2
        matriz[metade_matriz][0] = sm - 3

        removedor(matriz[0][0], lista_de_conferencia)
        removedor(matriz[metade_matriz][metade_matriz], lista_de_conferencia)
        removedor(matriz[metade_matriz][n_na_matriz], lista_de_conferencia)
        removedor(matriz[n_na_matriz][metade_matriz], lista_de_conferencia)
        removedor(matriz[0][metade_matriz], lista_de_conferencia)
        removedor(matriz[n_na_matriz][n_na_matriz], lista_de_conferencia)
        removedor(matriz[metade_matriz][0], lista_de_conferencia)

        
        mostrar('valores fixos', 1, matriz)


        c = int((n+1)/2)
        p = n - 1
        for i in range(n): #primeira diagonal
            c = c - 1
            matriz[i][p-i] = z - c
            removedor(matriz[i][p-i], lista_de_conferencia)

        for i in range(metade_matriz-1): #segunda diagonal
            matriz[i+1][i+1] = matriz[i][i] + n
            removedor(matriz[i+1][i+1], lista_de_conferencia)

        for i in range(n_na_matriz, metade_matriz+1, -1): #segunda diagonal
            matriz[i-1][i-1] = matriz[i][i] - n
            removedor(matriz[i-1][i-1], lista_de_conferencia)
        mostrar('diagonal', 2, matriz)

        for i in range(metade_matriz-1): #coluna central
            matriz[i+1][metade_matriz] = matriz[i][metade_matriz] - n
            removedor(matriz[i+1][metade_matriz], lista_de_conferencia)

        for i in range(n_na_matriz, metade_matriz+1, -1): #coluna central
            matriz[i-1][metade_matriz] = matriz[i][metade_matriz] + n
            removedor(matriz[i-1][metade_matriz], lista_de_conferencia)

        mostrar('coluna central', 3, matriz)

        for i in range(metade_matriz-1): #linha central
            matriz[metade_matriz][i+1] = matriz[metade_matriz][i] - n
            removedor(matriz[metade_matriz][i+1], lista_de_conferencia)

        for i in range(n_na_matriz, metade_matriz+1, -1): #linha central
            matriz[metade_matriz][i-1] = matriz[metade_matriz][i] + n
            removedor(matriz[metade_matriz][i-1], lista_de_conferencia)

        mostrar('linha central', 4, matriz)

        #ordem crescente    
        w=0
        l1 = n_na_matriz
        l2 = 0
        while contador(lista_de_conferencia) > 0:


            while True:
                a = 0

                for j in range(metade_matriz):
                    if matriz[j][l2] == ' ':
                        matriz[j][l2] = menor(lista_de_conferencia)
                        matriz[j][l1] = sm - matriz[j][l2]
                        removedor(matriz[j][l2], lista_de_conferencia)
                        removedor(matriz[j][l1], lista_de_conferencia)
                        break

                for j in range(n_na_matriz, metade_matriz, -1):
                    if matriz[j][l1] == ' ':
                        matriz[j][l1] = menor(lista_de_conferencia)
                        matriz[j][l2] = sm - matriz[j][l1]
                        removedor(matriz[j][l1], lista_de_conferencia)
                        removedor(matriz[j][l2], lista_de_conferencia)
                        a += 1
                        break

                if a == 0:
                    break
                
            while True:
                a = 0

                for j in range(metade_matriz):
                    if matriz[l1][j] == ' ':
                        matriz[l1][j] = menor(lista_de_conferencia)
                        matriz[l2][j] = sm - matriz[l1][j]
                        removedor(matriz[l1][j], lista_de_conferencia)
                        removedor(matriz[l2][j], lista_de_conferencia)
                        break

                for j in range(n_na_matriz, metade_matriz, -1):
                    if matriz[l2][j] == ' ':
                        matriz[l2][j] = menor(lista_de_conferencia)
                        matriz[l1][j] = sm - matriz[l2][j]
                        removedor(matriz[l2][j], lista_de_conferencia)
                        removedor(matriz[l1][j], lista_de_conferencia)
                        a += 1
                        break

                if a == 0:
                    break
                
            l1 -= 1 
            l2 += 1
        print('preenchimento', 5, matriz)
        # mostrar(matriz)
        verificador(matriz, cm, st)
    quadrado = matriz



janela = Tk()

janela.title('Quadrados Mágicos')

texto = Label(janela, text='digite o valor de "n" para o quadrado mágico:')
texto.grid(column=0, row=0, columnspan=num-1, pady=10)

valor_n = Entry(janela, width=5)
valor_n.grid(row=0, column=num-1)


botao = Button(janela, text='Criar Quadrado', command=algoritmo)
botao.grid(column=0, row=1, columnspan=num, pady=10)

texto_quadrado1 = Label(janela, text='')
matriz_quadrado1 = Label(janela, text='')
texto_quadrado1.grid(column=0, row=2, pady=5, columnspan=num)
matriz_quadrado1.grid(column=0, row=3, pady=10)

texto_quadrado2 = Label(janela, text='')
matriz_quadrado2 = Label(janela, text='')
texto_quadrado2.grid(column=0, row=3+num, pady=5, columnspan=num)
matriz_quadrado2.grid(column=0, row=4+num, pady=10)

texto_quadrado3 = Label(janela, text='')
matriz_quadrado3 = Label(janela, text='')
texto_quadrado3.grid(column=0, row=4+(num*2), pady=5, columnspan=num)
matriz_quadrado3.grid(column=0, row=5+(num*2), pady=10)

texto_quadrado4 = Label(janela, text='')
matriz_quadrado4 = Label(janela, text='')
texto_quadrado4.grid(column=0, row=5+(num*3), pady=5, columnspan=num)
matriz_quadrado4.grid(column=0, row=6+(num*3), pady=10)

texto_quadrado5 = Label(janela, text='')
matriz_quadrado5 = Label(janela, text='')
texto_quadrado5.grid(column=0, row=6+(num*4), pady=5, columnspan=num)
matriz_quadrado5.grid(column=0, row=7+(num*4), pady=10)

texto_verificacao = Label(janela, text='')
texto_verificacao.grid(column=0, row=8+(num*5), columnspan=num)

janela.mainloop()