// Fa�a um algoritmo que calcule se o elevador pode ou n�o transportar os alunos:
// O n�mero de alunos permitidos por viagem � 10.

programa questao{
  funcao inicio() {

    inteiro numero

    escreva ("Digite o n�mero de alunos: ")
    leia(numero)
    
    se (numero <= 10) {
        escreva("Sim, � permitido!")
    }
    senao {
        escreva("N�o � permitido!")
    }

  }
}