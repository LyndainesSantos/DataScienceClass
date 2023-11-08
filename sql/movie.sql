-- (movie) Qual a quantidade de filmes produzidos no ano de 2019?
select count(*) as qtde from movie where year = 2019;

-- (movie) Qual o país com maior frequência de produção de filmes?
select country, count(*) as qtde from movie group by country order by qtde desc limit 1;

-- (movie e genre) Qual a média de duração dos filmes produzidos com linguagem "German" e do gênero "Drama", somente.
select round(avg(m.duration),2) as media_duracao
from movie m join genre g
on m.id = g.movie_id
where m.languages = 'German' and g.genre = 'Drama';

-- (movie e ratings) Qual o filme mais bem avaliado (com maior avg_rating). Caso ocorra mais de um resultado para o mesmo avg_rating, considerar o filme
-- com maior quantidade de votos?
select m.title, r.avg_rating, r.total_votes
from movie m join ratings r
on m.id = r.movie_id
order by r.avg_rating desc, r.total_votes desc limit 1;
show columns from movie;