// Escreva um algoritmo que receba como entrada dois n�meros inteiros. Os n�meros devem ser armazenados nas vari�veis A e B. O algoritmo deve efetuar a troca dos valores de forma que a vari�vel A passe a ter o valor da vari�vel B e a vari�vel B passe a ter o valor da vari�vel A. Ao final, o algoritmo deve imprimir os valores trocados.

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

    escreva("O novo valor de A � ", A)
    escreva("\nO novo valor de B � ", B)
  }
}