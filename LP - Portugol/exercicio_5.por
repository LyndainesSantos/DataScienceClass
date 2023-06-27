// Calcule o IMC de uma pessoa: IMC = peso / altura²

programa {
  funcao inicio() {

    real peso=70, altura=1.70, imc

    imc = peso / (altura * altura)

    escreva("O IMC é igual a ", imc)
  }
}