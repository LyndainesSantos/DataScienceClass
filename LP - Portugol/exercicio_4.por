// Calcule o salário líquido de um professor. Os dados fornecidos são: valor da hora aula, número de aulas dadas no mês e percentual de desconto do INSS.

programa {
  funcao inicio() {

    real salario_liquido, salario_bruto, hora_aula=50, numero_aulas=16, percentual_desconto=10, perc2numero

    perc2numero = percentual_desconto/100
    salario_bruto = hora_aula * numero_aulas
    salario_liquido =  salario_bruto - (salario_bruto*perc2numero )
    
    escreva("O salário líquido é "+ salario_liquido)
  }
}