// Faça um algoritmo que leia 5 números e faça a soma entre eles.

programa questao{
  funcao inicio() {

    inteiro i, numero, soma = 0

    para(i = 0; i < 5; i++){
      escreva("Digite um número: ")
      leia(numero)

      soma = soma + numero
    }

    escreva("A soma é ", soma)

  }
}