def calcular_media(nota1:str, nota2:dict) -> dict:
    '''Retorna uma saudação personalizada '''
    media = (nota1 + nota2)/2
    situacao = "Aprovado" if media >= 7 else "Reprovado"
    return media, situacao

for media, situacao in [calcular_media(7,8)]:
    print(media, situacao)