// Escreva um algoritmo que receba como entrada dois números inteiros. Os números devem ser armazenados nas variáveis A e B. O algoritmo deve efetuar a troca dos valores de forma que a variável A passe a ter o valor da variável B e a variável B passe a ter o valor da variável A. Ao final, o algoritmo deve imprimir os valores trocados.

programa questao07{
  funcao inicio() {

    inteiro A,B,copy_A

    escreva("Digite o valor de A: ")
    leia(A)
    escreva("Digite o valor de B: ")
    leia(B)

    copy_A = A
    A=B
    B = copy_A

    escreva("O novo valor de A é ", A)
    escreva("\nO novo valor de B é ", B)
  }
}