// Fa�a um programa que leia 6 n�meros inteiros e no final mostre quantos s�o pares e quantos s�o �mpares.

programa questao{
  funcao inicio() {

    inteiro numero, i, cont_par=0, cont_impar=0

    para(i = 0; i < 6; i++){
      escreva("Digite um n�mero: ")
      leia(numero)

      se (numero%2 == 0) {
        cont_par = cont_par + 1
      }senao {
        cont_impar = cont_impar + 1
      }

    }

    escreva("N�meros pares: ", cont_par)
    escreva("\nN�meros �mpares: ", cont_impar)

  }
}