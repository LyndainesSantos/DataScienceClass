// Construa um algoritmo que receba um n�mero inteiro como entrada e imprima o sucessor e antecessor desse n�mero

programa{
  funcao inicio() {

    inteiro numero, antecessor, sucessor

    escreva("Digite um n�mero inteiro: ")
    leia(numero)

    antecessor = numero - 1
    sucessor = numero + 1

    escreva("O antecessor �: ", antecessor, "\n")
    escreva("O sucessor �: ", sucessor, "\n")

}
