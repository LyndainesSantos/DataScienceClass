// Escreva um algoritmo em pseudocódigo que calcule o valor de uma prestação em atraso, utilizando a seguinte fórmula:

programa {
  funcao inicio() {

    real prestacao, parcela, taxa
    inteiro tempo

    escreva("Digite o valor da parcela: ")
    leia(parcela)
    escreva("Digite a taxa: ")
    leia(taxa)
    escreva("Digite o tempo de atraso da prestação: ")
    leia(tempo)

    prestacao = parcela + (parcela*(taxa/100)*tempo)
    
    escreva("O valor da prestação, com ", tempo, " dias em atraso e taxa de ", taxa, "%, é igual a R$ ", prestacao)
  }
}