# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma
# mensagem de erro e voltando a pedir as informações.

while True:
    usuario = input("Digite o seu usuário: ").lower()
    senha = input("Digite a senha: ").lower()
    if(usuario == senha):
        print("Padrão Inválido!")
    else:
        break