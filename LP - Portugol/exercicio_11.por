// Faça um algoritmo que calcule se o elevador pode ou não transportar os alunos:
// O número de alunos permitidos por viagem é 10.

programa questao{
  funcao inicio() {

    inteiro numero

    escreva ("Digite o número de alunos: ")
    leia(numero)
    
    se (numero <= 10) {
        escreva("Sim, é permitido!")
    }
    senao {
        escreva("Não é permitido!")
    }

  }
}