# SPRINT 2

## SQL para Análise de Dados: Do básico ao avançado
# SQL para Análise de Dados: Do básico ao avançado

## Módulo 1 - Comandos básicos

### Comando SELECT

O comando SELECT é usado para selecionar dados de uma ou mais tabelas. A sintaxe do comando SELECT é a seguinte:

```
SELECT [column_list]
FROM [table_list]
WHERE [condition];
```

O **column_list** é uma lista de nomes de colunas que você deseja selecionar. O **table_list** é uma lista de nomes de tabelas das quais você deseja selecionar dados. O **condition** é uma condição que é usada para filtrar os dados que são selecionados.

Por exemplo, o seguinte comando SELECT seleciona todos os dados da tabela `customers`:

```
SELECT *
FROM customers;
```

O asterisco (*) significa que todos os dados da tabela serão selecionados.

O seguinte comando SELECT seleciona o nome e o e-mail dos clientes da tabela `customers`:

```
SELECT name, email
FROM customers;
```

O seguinte comando SELECT seleciona apenas os clientes que moram no estado da Califórnia da tabela `customers`:

```
SELECT name, email
FROM customers
WHERE state = 'CA';
```

### Comando WHERE

O comando WHERE é usado para filtrar os dados que são selecionados. A sintaxe do comando WHERE é a seguinte:

```
WHERE [condition];
```

A **condition** é uma condição que é usada para filtrar os dados que são selecionados. A condição pode ser uma expressão booleana, uma comparação ou uma cláusula IN.

Por exemplo, o seguinte comando SELECT seleciona apenas os clientes que moram no estado da Califórnia da tabela `customers`:

```
SELECT name, email
FROM customers
WHERE state = 'CA';
```

O seguinte comando SELECT seleciona apenas os clientes que têm um e-mail válido da tabela `customers`:

```
SELECT name, email
FROM customers
WHERE email IS NOT NULL AND email REGEXP '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$';
```

O seguinte comando SELECT seleciona apenas os clientes que têm um e-mail válido e moram no estado da Califórnia da tabela `customers`:

```
SELECT name, email
FROM customers
WHERE email IS NOT NULL AND email REGEXP '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$'
AND state = 'CA';
```

### Comando GROUP BY

O comando GROUP BY é usado para agrupar os dados que são selecionados. A sintaxe do comando GROUP BY é a seguinte:

```
GROUP BY [column_list];
```

A **column_list** é uma lista de colunas que você deseja agrupar. Os dados que são selecionados serão agrupados de acordo com os valores das colunas na **column_list**.

Por exemplo, o seguinte comando SELECT agrupa os clientes da tabela `customers` pelo estado e conta o número de clientes em cada estado:

```
SELECT state, COUNT(*) AS num_customers
FROM customers
GROUP BY state;
```

O resultado do comando SELECT será uma tabela com duas colunas: `state` e `num_customers`. A coluna `state` conterá os estados e a coluna `num_customers` conterá o número de clientes em cada estado.

### Comando ORDER BY

O comando ORDER BY é usado para ordenar os dados que são selecionados. A sintaxe do comando ORDER BY é a seguinte:

```
ORDER BY [column_list] [ASC | DESC];
```

A **column_list** é uma lista de colunas que você deseja ordenar. A palavra-chave `ASC` ordena os dados em ordem ascendente e a palavra-chave `DESC` ordena os dados em ordem descendente.

Por exemplo, o seguinte comando SELECT ordena os clientes da tabela `customers` pelo nome em ordem ascendente:

```
SELECT name, email
FROM customers
ORDER BY name ASC;
```

O resultado do comando SELECT será uma lista de clientes com os nomes ordenados em ordem ascendente.

O seguinte comando SELECT ordena os clientes da tabela `customers` pelo nome em ordem descendente:

```
SELECT name, email
FROM customers
ORDER BY name DESC;
```

### Modulo 2 - Operadores

	Claro, aqui está o arquivo readme com explicações simples e objetivas do texto que você forneceu:

# Operadores SQL

Este documento descreve os operadores SQL mais comuns e como usá-los.

## Operadores aritméticos

Os operadores aritméticos são usados para realizar operações matemáticas em valores. Eles incluem:

* + (adição)
* - (subtração)
* * (multiplicação)
* / (divisão)
* ^ (potenciação)
* % (módulo)

Por exemplo, a consulta a seguir calcula a idade de um cliente com base na data de nascimento:

```
SELECT (CURRENT_DATE - birth_date) / 365 AS age
FROM customers;
```

## Operadores relacionais

Os operadores relacionais são usados para comparar dois valores e retornar um valor booleano (TRUE ou FALSE). Eles incluem:

* = (igual)
* > (maior que)
* < (menor que)
* >= (maior ou igual a)
* <= (menor ou igual a)
* <> (diferente de)

Por exemplo, a consulta a seguir seleciona todos os clientes cuja idade é maior que 18 anos:

```
SELECT *
FROM customers
WHERE age > 18;
```

## Operadores lógicos

Os operadores lógicos são usados para combinar duas ou mais expressões booleanas. Eles incluem:

* AND (e)
* OR (ou)
* NOT (não)

Por exemplo, a consulta a seguir seleciona todos os clientes que são do sexo masculino e têm mais de 18 anos:

```
SELECT *
FROM customers
WHERE gender = 'male'
AND age > 18;
```

## Operadores de junção

Os operadores de junção são usados para combinar linhas de duas ou mais tabelas. Eles incluem:

* INNER JOIN (junção interna)
* LEFT JOIN (junção externa esquerda)
* RIGHT JOIN (junção externa direita)
* FULL JOIN (junção completa)

Por exemplo, a consulta a seguir seleciona todos os pedidos e os produtos correspondentes:

```
SELECT *
FROM orders
INNER JOIN products ON orders.product_id = products.id;
```

## Outros operadores

Existem outros operadores SQL que não são tão comuns, mas que podem ser úteis em certas situações. Esses operadores incluem:

* IS NULL (é nulo)
* IS NOT NULL (não é nulo)
* IN (está incluído)
* BETWEEN (entre)
* LIKE (semelhante)
* ILIKE (semelhante, ignorando maiúsculas e minúsculas)

# Funções Agregadas

As funções agregadas são usadas para executar operações matemáticas em um conjunto de valores. Elas são normalmente usadas para agrupar e sumarizar dados.

## Tipos de funções agregadas

Há muitas funções agregadas diferentes, mas algumas das mais comuns são:

* COUNT() - Conta o número de linhas em um conjunto de dados
* SUM() - Soma os valores em um conjunto de dados
* MIN() - Encontra o valor mínimo em um conjunto de dados
* MAX() - Encontra o valor máximo em um conjunto de dados
* AVG() - Calcula a média dos valores em um conjunto de dados

## Exemplos de uso de funções agregadas

Aqui estão alguns exemplos de como as funções agregadas podem ser usadas:

* Para contar o número de clientes em uma tabela:

```
SELECT COUNT(*) AS total_clients
FROM customers;
```

* Para somar o valor total de todas as vendas em uma tabela:

```
SELECT SUM(price) AS total_sales
FROM orders;
```

* Para encontrar o valor mínimo de todos os preços em uma tabela:

```
SELECT MIN(price) AS min_price
FROM products;
```

* Para encontrar o valor máximo de todos os preços em uma tabela:

```
SELECT MAX(price) AS max_price
FROM products;
```

* Para calcular a média dos preços em uma tabela:

```
SELECT AVG(price) AS avg_price
FROM products;
```

## Usando o GROUP BY

O GROUP BY é usado para agrupar linhas de dados em um conjunto de dados com base em um conjunto de critérios. Isso pode ser útil para sumarizar dados ou para encontrar padrões em um conjunto de dados.

Aqui está um exemplo de como o GROUP BY pode ser usado para agrupar os clientes por estado:

```
SELECT state, COUNT(*) AS total_clients
FROM customers
GROUP BY state;
```

A consulta acima retornará uma tabela com dois campos: o estado e o número total de clientes em cada estado.

## Usando o HAVING

O HAVING é usado para filtrar os resultados de uma consulta que usa o GROUP BY. Isso pode ser útil para remover linhas que não atendem a certos critérios.

Aqui está um exemplo de como o HAVING pode ser usado para filtrar os resultados da consulta anterior para remover estados com menos de 100 clientes:

```
SELECT state, COUNT(*) AS total_clients
FROM customers
GROUP BY state
HAVING total_clients > 100;
```

A consulta acima retornará apenas os estados com mais de 100 clientes.
