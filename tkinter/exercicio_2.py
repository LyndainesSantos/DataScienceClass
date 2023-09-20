# Write a Python GUI program to add a button in your application using tkinter module.
from tkinter import *
janela = Tk()
janela.title("Exemplo 2")
janela.geometry('800x300')
def ler_entrada():
    # label2.config(text=f'Olá, {entrada.get().title()}!')
    label2['text'] = f'Olá, {entrada.get().title()}!'
    entrada.delete(0, 'end')
label1 = Label(
    master=janela,
    text='Digite seu nome: ',
    font = 14
)
label1.grid(row=0, column=0, padx=10, pady=10)

entrada = Entry(
    master=janela,
    width=30,
    font=('Arial', 12)
)
entrada.grid(row = 0, column = 1, padx = 10, pady = 10, sticky=NSEW)
botao = Button(
    master=janela,
    text='Ok',
    width=10,
    background='gray',
    font=('Arial', 14),
    command=ler_entrada
    )
botao.grid(row=0, column=2, padx=10, pady=10, sticky=NSEW)
label2 = Label(
    master=janela,
    text='',
    font=('Arial', 14)
)
label2.grid(row=1, column=1, padx=10, pady=30, sticky=NSEW)
janela.mainloop()