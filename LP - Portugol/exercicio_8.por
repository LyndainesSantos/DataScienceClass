// Escreva um algoritmo que calcule o volume de uma lata de óleo, utilizando a seguinte fórmula: volume=3.14 × R² ×altura

programa questao08{
  funcao inicio() {

    real volume, r, h, pi=3.14

    escreva("Digite o raio: ")
    leia(r)
    escreva("Digite a altura: ")
    leia(h)
    
    volume = pi * r * r * h
    
    escreva("O volume da lata de óleo é ", volume)
  }
}