// Fa�a um algoritmo que calcule a m�dia de um aluno que fez 3 provas e se for maior que 7, mostre a mensagem de "Aprovado"

programa questao{
  funcao inicio() {

    real nota1, nota2, nota3, media

    escreva ("Digite a primeira nota : ")
    leia (nota1)
    escreva ("Digite a segunda nota : ")
    leia (nota2)
    escreva ("Digite a terceira nota : ")
    leia (nota3)

    media=(nota1+nota2+nota3)/3

    escreva ("A m�dia do aluno foi ", media)

    se (media>7){
      escreva ("\n  Aprovado!")
    }
    senao {
      escreva ("\n Reprovado!")
    }

  }
}