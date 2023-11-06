# Implemente uma função lambda que receba duas strings e retorne a concatenação
# das duas, apenas se ambas as strings tiverem mais de 5 caracteres. Caso contrário,
# a função deve retornar uma mensagem de erro.

resultado = lambda x, y: x+y if len(x) > 5 and len(y) > 5 else ("erro: o tamanho das strings é "
                                                                "menor que 5")
print(resultado("school", "infinity"))
print(resultado("dev", "stack"))