# Considerando o dicionario abaixo:
estados_habitantes = {
    "Ceará": 8.843*10**6,
    "Piauí": 3.195*10**6,
    "Minas Gerais": 20.87*10**6,
    "Santa Catarina": 7.165*10**6
}

# a) Acesse a capital do estado de Minas gerais e armazene em uma variável chamada capital_MG.

habitantes = estados_habitantes["Minas Gerais"]

# b) Adicione um novo estado ao dicionário com a sua respectiva quantidade populacional.

estados_habitantes["Bahia"] = 15.13*10**6

# c) Crie uma função que recebe um dicionário como argumento e retorna o nome do estado e da
# capital com maior número de habitantes.
def maior_populacao(dicionario:dict):

    max_habitantes= max(dicionario.values())
    estado_max_habitantes = "Default"
    for estado,habitantes in dicionario.items():
        if habitantes == max_habitantes:
            estado_max_habitantes = estado

    return estado_max_habitantes,max_habitantes

e,h = maior_populacao(estados_habitantes)

print(f"O estado {e} possui o maior contingente populacional, com {h} habitantes")