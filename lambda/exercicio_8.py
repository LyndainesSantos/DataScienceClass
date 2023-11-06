# A partir de uma lista de dicionários, cada um representando uma pessoa com os campos
# "nome" e "idade", utilize map() e uma função lambda para obter uma nova lista
# contendo apenas os nomes das pessoas.
lista = [
            {"nome": "Maria", "idade": 30},
            {"nome": "José", "idade": 90},
            {"nome": "Ana", "idade": 50},
         ]
resultado = list(map(lambda x: x["nome"], lista))
print(resultado)