// Escreva um algoritmo que receba um número com quatro dígitos e imprima o primeiro e último digito.

programa questao10{
  funcao inicio() {

    inteiro numero, primeiro, ultimo

    escreva("Digite um número com quatro dígitos: ")
    leia(numero)

    primeiro = numero/1000
    ultimo = numero%10
    
    escreva("O primeiro dígito é ", primeiro)
    escreva("\nO último dígito é ", ultimo)
  }
}