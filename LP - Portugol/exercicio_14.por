// Fa�a um algoritmo que leia 5 n�meros e fa�a a soma entre eles.

programa questao{
  funcao inicio() {

    inteiro i, numero, soma = 0

    para(i = 0; i < 5; i++){
      escreva("Digite um n�mero: ")
      leia(numero)

      soma = soma + numero
    }

    escreva("A soma � ", soma)

  }
}