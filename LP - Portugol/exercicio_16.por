// Faça um programa que leia 6 números inteiros e no final mostre quantos são pares e quantos são ímpares.

programa questao{
  funcao inicio() {

    inteiro numero, i, cont_par=0, cont_impar=0

    para(i = 0; i < 6; i++){
      escreva("Digite um número: ")
      leia(numero)

      se (numero%2 == 0) {
        cont_par = cont_par + 1
      }senao {
        cont_impar = cont_impar + 1
      }

    }

    escreva("Números pares: ", cont_par)
    escreva("\nNúmeros ímpares: ", cont_impar)

  }
}