// Escreva um algoritmo em pseudoc�digo que calcule o valor de uma presta��o em atraso, utilizando a seguinte f�rmula:

programa {
  funcao inicio() {

    real prestacao, parcela, taxa
    inteiro tempo

    escreva("Digite o valor da parcela: ")
    leia(parcela)
    escreva("Digite a taxa: ")
    leia(taxa)
    escreva("Digite o tempo de atraso da presta��o: ")
    leia(tempo)

    prestacao = parcela + (parcela*(taxa/100)*tempo)
    
    escreva("O valor da presta��o, com ", tempo, " dias em atraso e taxa de ", taxa, "%, � igual a R$ ", prestacao)
  }
}