// Faça um programa que leia o valor inicial da contagem, o valor final e o incremento, mostrando em seguida todos os valores deste intervalo. 


programa questao{
  funcao inicio() {

    inteiro numero_inicial, numero_final, incremento, i

    escreva("Digite o número inicial: ")
    leia(numero_inicial)
    escreva("Digite o número final: ")
    leia(numero_final)
    escreva("Digite o incremento: ")
    leia(incremento)

    para(i = numero_inicial; i < numero_final; i=i+incremento){
      escreva(i," , ")
    }

  }
}