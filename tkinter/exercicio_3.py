from tkinter import *
from banco_dados import banco
from tkinter import messagebox

janela = Tk()
janela.title('Tela de Login')
janela.geometry('330x450+500+150')
janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)
janela.resizable(False, False)

cor_fundo = '#B0E0E6'
cor_botao = '#00CED1'

def mostrar_senha():
    print(mostrar)
    if mostrar.get() == True:
        entrada_senha['show'] = ''
    else:
        entrada_senha['show'] = '*'
def credenciais():
    db = banco()
    user = db['user'].get(entrada_email.get())
    if not user:
        print("Usuário não cadastrado")
        messagebox.showerror("Erro", "Usuário não cadastrado!")
    else:
        if user['senha'] != entrada_senha.get():
            print("Senha incorreta")
            messagebox.showerror("Erro", "Senha incorreta!")
        else:
            messagebox.showinfo("Sucesso!", "Login realizado com sucesso!")
            print(user)

frame = Frame(
    master = janela,
    background = cor_fundo
)
frame.grid(sticky=NSEW)

label = Label(
    master=frame,
    text='Login',
    justify='center',
    font=('Times New Roman', 34),
    bg = cor_fundo
)
label.grid(pady=40, sticky=NSEW)

label_email = Label(
    master=frame,
    text='E-mail *',
    font=('Times New Roman', 14),
    bg = cor_fundo
)
label_email.grid(padx= 10, sticky=W)

entrada_email = Entry(
    master=frame,
    width=50
)
entrada_email.grid(padx=10, pady=10, sticky=NSEW)
entrada_email.focus()

label_senha = Label(
    master=frame,
    text='Senha *',
    font=('Times New Roman', 14),
    bg=cor_fundo
)
label_senha.grid(padx=10, sticky=W)

mostrar = IntVar()
# mostrar = BooleanVar()
check_senha = Checkbutton(
    master=frame,
    text='Mostrar senha',
    font=('Times New Roman', 9),
    variable=mostrar,
    bg=cor_fundo,
    command=mostrar_senha

)
check_senha.grid(sticky=W, padx=10)

entrada_senha = Entry(
    master=frame,
    show='*',
    width=50
)
entrada_senha.grid(padx=10, sticky=E)

botao = Button(
    master=frame,
    text='Entrar',
    font=('Times New Roman', 14),
    width= 10,
    bg = cor_botao,
    command=credenciais
)
botao.grid(padx=10, pady=30, sticky = N)
janela.mainloop()