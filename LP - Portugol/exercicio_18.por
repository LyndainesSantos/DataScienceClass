// Uma empresa precisa reajustar o sal�rio dos seus funcion�rios, dando um aumento de acordo com alguns fatores. Fa�a um programa que leia o sal�rio atual, 
// o g�nero do funcion�rio e h� quantos anos esse funcion�rio trabalha na empresa. No final, mostre o seu novo sal�rio, baseado na tabela a seguir:
// Mulheres:
// menos de 15 anos de empresa: +5%
// de 15 at� 20 anos de empresa: +12%
// mais de 20 anos de empresa: +23%
// Homens:
// menos de 20 anos de empresa: +3%
// de 20 at� 30 anos de empresa: +13%
// mais de 30 anos de empresa: +25%


programa questao{
  funcao inicio() {

    cadeia genero
    real tempo, salario_atual, salario_ajustado, acrescimo
		
    escreva("Qual o g�nero: ")
    leia(genero)
    escreva("Qual o tempo de trabalho: ")
    leia(tempo)
    escreva("Qual o seu atual sal�rio: ")
    leia(salario_atual)

    se(genero == "F" ou genero == "f"){

      se(tempo < 15){
        acrescimo = salario_atual*5/100
      }senao se(tempo>15 e tempo < 20){
        acrescimo = salario_atual*12/100
      } senao {
        acrescimo = salario_atual*23/100
      }

    }senao se(genero == "M" ou genero == "m") {

      se(tempo < 20){
        acrescimo = salario_atual*3/100
      }senao se(tempo>20 e tempo < 30){
        acrescimo = salario_atual*13/100
      } senao {
        acrescimo = salario_atual*25/100
      }

    }

    salario_ajustado = salario_atual + acrescimo
    
    escreva("O novo sal�rio, ajustado, � igual a R$ ", salario_ajustado)
  }
}