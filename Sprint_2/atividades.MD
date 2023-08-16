# Tabela Biblioteca

### 1 - Apresente a query para listar todos os livros publicados após 2014. Ordenar pela coluna cod, em ordem crescente, as linhas.  Atenção às colunas esperadas no resultado final: cod, titulo, autor, editora, valor, publicacao, edicao, idioma

```sql
SELECT cod, titulo, autor, editora, valor, publicacao, edicao, idioma
FROM livro
WHERE publicacao > '2014-12-31'
ORDER BY cod;
```


### 2 - Apresente a query para listar os 10 livros mais caros. Ordenar as linhas pela coluna valor, em ordem decrescente.  Atenção às colunas esperadas no resultado final:  titulo, valor.

```sql
SELECT titulo, valor
FROM livro
ORDER BY valor DESC
LIMIT 10;
```


### 3 - Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.

```sql
SELECT COUNT(*) AS quantidade, nome, estado, cidade
FROM editora
INNER JOIN livro ON codEditora = editora
INNER JOIN endereco ON codEndereco = endereco
GROUP BY codEditora
ORDER BY quantidade DESC
LIMIT 5;
```


### 4 - Apresente a query para listar a quantidade de livros publicada por cada autor. Ordenar as linhas pela coluna nome (autor), em ordem crescente. Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).

```sql
SELECT aut.nome, aut.codautor, aut.nascimento, COUNT(liv.titulo) AS quantidade
FROM autor AS aut
LEFT JOIN livro AS liv
ON aut.codautor = liv.autor
GROUP BY aut.nome
ORDER BY aut.nome;
```


### 5 - Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno.

```sql
SELECT autor.nome
FROM endereco
INNER JOIN editora ON editora.endereco = endereco.codendereco
INNER JOIN livro ON livro.editora = editora.codeditora
INNER JOIN autor ON autor.codautor = livro.autor
WHERE endereco.estado NOT IN ('PARANÁ', 'RIO GRANDE DO SUL', 'SANTA CATARINA')
GROUP BY autor.nome
ORDER BY autor.nome;
```


### 6 - Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.

```sql
SELECT livro.autor AS codautor, nome, COUNT(livro.titulo) AS quantidade_publicacoes
FROM autor
INNER JOIN livro ON autor.codautor = livro.autor
GROUP BY nome
ORDER BY quantidade_publicacoes DESC
LIMIT 1;
```


### 7 - Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.

```sql
SELECT autor.nome
FROM autor
LEFT JOIN livro ON autor.codautor = livro.autor
WHERE livro.titulo IS NULL
ORDER BY autor.nome;
```


# Tabela Loja

### 1 - Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.

```sql
SELECT tabela_vendedor.cdvdd, tabela_vendedor.nmvdd
FROM tbvendedor AS tabela_vendedor
LEFT JOIN tbvendas AS tabela_vendas
ON tabela_vendedor.cdvdd = tabela_vendas.cdvdd
WHERE tabela_vendas.status = 'Concluído'
GROUP BY tabela_vendedor.cdvdd, tabela_vendedor.nmvdd
ORDER BY COUNT(tabela_vendas.cdven) DESC
LIMIT 1;
```


### 2 - Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.

```sql
SELECT
    cdpro,
    nmpro
from tbvendas

WHERE status = 'Concluído'
AND dtven BETWEEN
    '2014-02-03' AND '2018-02-02'
GROUP BY
    cdpro,
    nmpro
ORDER BY
    COUNT(cdpro) DESC
limit 1
```

### 3 - A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído. As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.

```sql
SELECT
    nmvdd as vendedor,

    SUM(tbvendas.qtd * tbvendas.vrunt) as valor_total_vendas,
    ROUND(SUM(tbvendas.qtd * tbvendas.vrunt * tbvendedor.perccomissao)/100,2) AS comissao

from tbvendedor

left join tbvendas ON tbvendedor.cdvdd = tbvendas.cdvdd

WHERE tbvendas.status = 'Concluído'
GROUP BY
    tbvendedor.nmvdd
ORDER BY
    comissao DESC

```

### 4 - Apresente a query para listar o código e nome cliente com maior gasto na loja. As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.

```sql
SELECT
    tbvendas.cdcli,
    tbvendas.nmcli,
    SUM(tbvendas.qtd * tbvendas.vrunt) as gasto

FROM tbvendas

WHERE
    tbvendas.status = 'Concluído'
GROUP BY
    tbvendas.cdcli,
    tbvendas.nmcli

ORDER BY
    gasto DESC

LIMIT
    1
```

### 5 - Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.

```sql
SELECT
    tbdependente.cddep,
    tbdependente.nmdep,
    tbdependente.dtnasc,
    SUM(tbvendas.qtd * tbvendas.vrunt) AS valor_total_vendas
FROM
    tbdependente
LEFT JOIN
    tbvendas ON tbdependente.cdvdd = tbvendas.cdvdd

WHERE
    tbvendas.status = 'Concluído'
GROUP BY
    tbdependente.cddep
ORDER BY
    valor_total_vendas
limit
    1
```


### 6 - Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).  As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.

```sql

SELECT

    cdpro,
    nmcanalvendas,
    nmpro,
    SUM(qtd) AS quantidade_vendas

FROM
    tbvendas

WHERE
    status = 'Concluído'
GROUP BY
    cdpro,
    nmcanalvendas
ORDER BY
    quantidade_vendas,
    nmcanalvendas DESC
limit
    10
```

### 7 - Apresente a query para listar o gasto médio por estado da federação. As colunas presentes no resultado devem ser estado e gastomedio. Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.Observação: Apenas vendas com status concluído.

```sql
SELECT
    estado,
    ROUND(AVG(qtd * vrunt), 2) AS gastomedio

FROM
    tbvendas

WHERE
    status = 'Concluído'

GROUP BY
    estado
ORDER BY
    gastomedio DESC
```

### 8 - Apresente a query para listar os códigos das vendas identificadas como deletadas. Apresente o resultado em ordem crescente.

```sql
SELECT
    cdven
FROM
    tbvendas
WHERE
    deletado = 1
GROUP BY
    cdven
ORDER BY
    cdven;
```

### 9 -  Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. Considere arredondar o valor da coluna quantidade_media na quarta casa decimal. Ordene os resultados pelo estado (1º) e nome do produto (2º).

```sql

SELECT
    estado,
    nmpro,
    ROUND(AVG(qtd), 4) AS quantidade_media
FROM
    tbvendas
WHERE
    status = 'Concluído'
GROUP BY
    estado,
    nmpro
ORDER BY
    estado,
    nmpro
```