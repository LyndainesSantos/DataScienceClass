from tkinter import *
janela = Tk()
janela.title("Exemplo 1")
janela.geometry('500x300')
def ler_entrada():
    label2.config(text=f'Olá, {entrada.get()}!')
label1 = Label(
    master=janela,
    text='Digite seu nome: ',
    font = 14
)
label1.pack(pady=20)
entrada = Entry(
    master=janela,
    width=50,
    font=('Arial', 12)
)
entrada.pack(padx = 20, pady = 20)
entrada.focus()
botao = Button(
    master=janela,
    text='Ok',
    width=10,
    background='gray',
    font=('Arial', 14),
    command=ler_entrada
    )
botao.pack()
label2 = Label(
    master=janela,
    text='',
    font=('Arial', 14)
)
label2.pack(pady=30)
janela.mainloop()
