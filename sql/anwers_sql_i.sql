-- Exercício 1
select * from notas_fiscais where uf_emitente = 'SC';

-- Exercício 2
select sum(valor_total) as valor_total from notas_fiscais where uf_emitente = 'PI';

-- Exercício 3
select * from notas_fiscais where uf_emitente = 'SC' and valor_unit > 200;

-- Exercício 4
select uf_emitente, sum(valor_total) as total_vendas
from notas_fiscais
group by uf_emitente
order by total_vendas desc;

-- Exercício 5
select natureza_operacao, avg(valor_unit) as media_valor_unitario
from notas_fiscais
group by natureza_operacao;

-- Exercício 6
select * from city where population > 100000 and countrycode = 'USA';

-- Exercício 7
select name from city where population > 120000 and countrycode = 'USA';

-- Exercício 8
select city, char_length(city) from station order by char_length(city), city limit 1;
select city, char_length(city) from station order by char_length(city) desc, city limit 1;
