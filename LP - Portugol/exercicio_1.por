// Construa um algoritmo que receba um número inteiro como entrada e imprima o sucessor e antecessor desse número

programa{
  funcao inicio() {

    inteiro numero, antecessor, sucessor

    escreva("Digite um número inteiro: ")
    leia(numero)

    antecessor = numero - 1
    sucessor = numero + 1

    escreva("O antecessor é: ", antecessor, "\n")
    escreva("O sucessor é: ", sucessor, "\n")

}
