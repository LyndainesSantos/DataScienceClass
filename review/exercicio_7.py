# Faça um programa que leia e valide as seguintes informações:
# a. Nome: maior que 3 caracteres;
# b. Idade: entre 0 e 150;
# c. Salário: maior que zero;
# d. Sexo: 'f' ou 'm';
# e. Estado Civil: 's', 'c', 'v', 'd';

while True:

    nome = input("Digite seu nome: ")
    if(len(nome) < 3):
        continue

    idade = int(input("Digite sua idade: "))
    while(idade < 0 or idade > 150):
        idade = int(input("Digite sua idade: "))

    salario = float(input("Digite seu salário: "))
    while(salario <=0):
        salario = float(input("Digite seu salário: "))

    sexo = input("Digite seu genero: ")
    while(sexo != "m" and sexo != "f"):
        sexo = input("Digite seu genero: ")

    e_civil = input("Informe o seu estado civil: ")
    while(e_civil not in ("scvd")):
        e_civil = input("Informe o seu estado civil: ")

    break

print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Salário: R$ {salario}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {e_civil}")