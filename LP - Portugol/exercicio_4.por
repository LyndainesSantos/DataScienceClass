// Calcule o sal�rio l�quido de um professor. Os dados fornecidos s�o: valor da hora aula, n�mero de aulas dadas no m�s e percentual de desconto do INSS.

programa {
  funcao inicio() {

    real salario_liquido, salario_bruto, hora_aula=50, numero_aulas=16, percentual_desconto=10, perc2numero

    perc2numero = percentual_desconto/100
    salario_bruto = hora_aula * numero_aulas
    salario_liquido =  salario_bruto - (salario_bruto*perc2numero )
    
    escreva("O sal�rio l�quido � "+ salario_liquido)
  }
}