# Leia os dados de um usuário - nome, sobrenome, idade, email - e imprima-os enumerando os mesmos.

usuario = {}
usuario["nome"] = input("Digite o nome do usuário: ")
usuario["sobrenome"] = input("Digite o sobrenome do usuário: ")
usuario["idade"] = input("Digite a idade do usuário: ")
usuario["email"] = input("Digite o email do usuário: ")

print("Dados do usuário:")
for index, chave in enumerate(usuario, start=1):
    print(f"{index}. {chave.capitalize()}: {usuario[chave]}")