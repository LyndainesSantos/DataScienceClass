// Calcule o IMC de uma pessoa: IMC = peso / altura�

programa {
  funcao inicio() {

    real peso=70, altura=1.70, imc

    imc = peso / (altura * altura)

    escreva("O IMC � igual a ", imc)
  }
}