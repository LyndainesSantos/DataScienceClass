// Uma empresa precisa reajustar o salário dos seus funcionários, dando um aumento de acordo com alguns fatores. Faça um programa que leia o salário atual, 
// o gênero do funcionário e há quantos anos esse funcionário trabalha na empresa. No final, mostre o seu novo salário, baseado na tabela a seguir:
// Mulheres:
// menos de 15 anos de empresa: +5%
// de 15 até 20 anos de empresa: +12%
// mais de 20 anos de empresa: +23%
// Homens:
// menos de 20 anos de empresa: +3%
// de 20 até 30 anos de empresa: +13%
// mais de 30 anos de empresa: +25%


programa questao{
  funcao inicio() {

    cadeia genero
    real tempo, salario_atual, salario_ajustado, acrescimo
		
    escreva("Qual o gênero: ")
    leia(genero)
    escreva("Qual o tempo de trabalho: ")
    leia(tempo)
    escreva("Qual o seu atual salário: ")
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
    
    escreva("O novo salário, ajustado, é igual a R$ ", salario_ajustado)
  }
}