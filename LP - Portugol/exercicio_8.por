// Escreva um algoritmo que calcule o volume de uma lata de �leo, utilizando a seguinte f�rmula: volume=3.14 � R� �altura

programa questao08{
  funcao inicio() {

    real volume, r, h, pi=3.14

    escreva("Digite o raio: ")
    leia(r)
    escreva("Digite a altura: ")
    leia(h)
    
    volume = pi * r * r * h
    
    escreva("O volume da lata de �leo � ", volume)
  }
}