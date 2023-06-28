// Faça um algoritmo que converta a temperatura de Fahrenheit para celsius e diga se estar frio ou quente:
// c = (f - 32) / 1.8 .

programa questao{
  funcao inicio() {

    real f, c

    escreva ("Qual a temperatura em Fahrenheit? ")
    leia (f)

    c = (f - 32) / 1.8

    escreva("No Brasil, a temperatura é ", c)

  }
}