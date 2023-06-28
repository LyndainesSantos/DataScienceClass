// Faça um programa que mostre na tela a seguinte contagem: 100 95 90 85 80 ... 0 Acabou!
// **OBS**: contagem regressiva de 100 até 0 pulando a cada 5.

programa questao{
  funcao inicio() {

    inteiro i

    para(i = 100; i!=0; i=i-5){

      escreva(i, " ")

    }
    escreva("Acabou!")
  }
}