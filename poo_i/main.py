# exercício 1
from exercicio_4 import SysInformatica
item1 = SysInformatica("Teclado", 50.0, 3)
print(item1.gerarFatura())

# exercício 2
import exercicio_1
pessoa = exercicio_2.Pessoa("Maria", 40, "Fortaleza")
print(pessoa.exibir_infos())

# exercício 3
from exercicio_2 import ContaBancaria
objeto = ContaBancaria(1234, 500)
print(objeto.depositar(500))
print(objeto.sacar(200))

# exercicio 4
from exercicio_3 import Livro
objeto = Livro("Alice no país das maravilhas", "Não sei", 1978)
print(objeto.infos()['Título'])

# exercicio 5
from exercicio_5 import Triangulo
objeto = Triangulo(4,4,4)
print(objeto.area())
print(objeto.verificar())