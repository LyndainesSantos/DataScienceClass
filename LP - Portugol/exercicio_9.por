// Escreva um algoritmo que calcule o desconto de um produto. O novo valor deve possui um desconto de 12%

programa questao09{
  funcao inicio() {

    real valor, novo_valor, desc=12

    escreva("Informe o valor do produto: ")
    leia(valor)

    novo_valor = valor - (valor*(desc/100))
    
    escreva("O valor do produto com desconto é ", novo_valor)
  }
}