// Escreva um algoritmo que receba um n�mero com quatro d�gitos e imprima o primeiro e �ltimo digito.

programa questao10{
  funcao inicio() {

    inteiro numero, primeiro, ultimo

    escreva("Digite um n�mero com quatro d�gitos: ")
    leia(numero)

    primeiro = numero/1000
    ultimo = numero%10
    
    escreva("O primeiro d�gito � ", primeiro)
    escreva("\nO �ltimo d�gito � ", ultimo)
  }
}