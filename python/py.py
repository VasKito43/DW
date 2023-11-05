import tkinter as tk

def coletar_entrada():
    valor = entry.get()
    print("O valor inserido foi:", valor)

root = tk.Tk()
root.title("Coleta de Entrada no Tkinter")

# Função para coletar a entrada ao pressionar o botão
entry = tk.Entry(root)
entry.pack()

botao = tk.Button(root, text="Coletar", command=coletar_entrada)
botao.pack()

root.mainloop()
