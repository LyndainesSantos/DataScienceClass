-- Exercício 1
# Faça uma consulta que mostre a descrição e o estoque do produto e o nome do fornecedor do produto
select p.descricao, p.estoque, f.razao_social
from produto p join fornecedor f
on p.CNPJ_Fornecedor = f.CNPJ;

-- Exercício 2
# Faça uma consulta que mostra o número, data e o nome do cliente de todas as notas
select nota.numero, nota.data, cliente.nome
from nota left join cliente
on nota.Codigo_Cliente = cliente.Codigo;

-- Exercício 3
# Faça uma consulta que mostre o nome do cliente e a soma das notas desse cliente
select cliente.Nome, sum(produto.Valor * item.Qtde) as valor_nota
from cliente join nota
on nota.Codigo_Cliente = cliente.Codigo
join item
on item.Numero_Nota = nota.Numero
join produto
on item.Codigo_Produto = produto.Codigo
group by cliente.Nome;

-- Exercício 4
# Faça uma consulta que mostre os fornecedores que tenham produtos com estoque igual a 0 ou Null
select fornecedor.CNPJ, produto.Estoque
from fornecedor left join produto
on fornecedor.CNPJ = produto.CNPJ_Fornecedor
where produto.Estoque = 0 or produto.Estoque is null;

-- Exercício 5
# Faça uma consulta que mostre o valor total das notas por tipo de pagamento
select nota.tipo_pagto, sum(produto.valor * item.qtde) as valor_total_notas
from nota left join item
on nota.Numero = item.Numero_Nota
left join produto
on produto.Codigo = item.Codigo_Produto
group by nota.Tipo_Pagto;

-- Exercício 6
# Refaça o exercício 2 organizando o resultado pela ordem alfabética do nome do cliente e caso o nome seja nulo, deve ser posicionado por último
select nota.numero, nota.data, cliente.nome
from nota left join cliente
on nota.Codigo_Cliente = cliente.Codigo
order by 
case
	when cliente.Nome is null then 1
    else 0
end,
cliente.Nome;
