# SPRINT 2

## SQL para Análise de Dados: Do básico ao avançado

Claro, aqui estão alguns exemplos dos comandos em ação:

* `select email from sales.customers`

> `SELECT email FROM sales.customers;`

A saída será uma lista de todos os emails na tabela `sales.customers`:

```
john.doe@gmail.com
mary.smith@yahoo.com
steven.jackson@hotmail.com
```

* `select email, first_name, last_name from sales.customers`

> `SELECT email, first_name, last_name FROM sales.customers;`

A saída será uma lista de todos os clientes na tabela `sales.customers`, com seus emails, nomes e sobrenomes:

```
email | first_name | last_name
-------|------------|------------
john.doe@gmail.com | John | Doe
mary.smith@yahoo.com | Mary | Smith
steven.jackson@hotmail.com | Steven | Jackson
```

* `select * from sales.customers`

> `SELECT * FROM sales.customers;`

A saída será uma lista de todos os dados na tabela `sales.customers`, incluindo as colunas `email`, `first_name`, `last_name` e todas as outras:

```
id | email | first_name | last_name | state | birth_date | score
-------|------------|------------|------------|-------|------------|-------
1 | john.doe@gmail.com | John | Doe | MS | 1980-01-01 | 100
2 | mary.smith@yahoo.com | Mary | Smith | SC | 1981-02-02 | 95
3 | steven.jackson@hotmail.com | Steven | Jackson | GA | 1982-03-03 | 90
```

* `select distinct brand from sales.products`

> `SELECT DISTINCT brand FROM sales.products;`

A saída será uma lista de todas as marcas distintas na tabela `sales.products`:

```
brand
-------
Apple
Samsung
Sony
```

* `select distinct brand, model_year from sales.products`

> `SELECT DISTINCT brand, model_year FROM sales.products;`

A saída será uma lista de todas as marcas e anos de modelo distintos na tabela `sales.products`:

```
brand | model_year
-------|------------
Apple | 2023
Apple | 2022
Samsung | 2023
```

* `select email, state from sales.customers where state = 'MS'`

> `SELECT email, state FROM sales.customers WHERE state = 'MS';`

A saída será uma lista de todos os clientes no Mississippi, com seus emails e estados:

```
email | state
-------|-------
john.doe@gmail.com | MS
steven.jackson@hotmail.com | MS
```

* `select email, state from sales.customers where state = 'SC' or state = 'MS'`

> `SELECT email, state FROM sales.customers WHERE state = 'SC' OR state = 'MS';`

A saída será uma lista de todos os clientes no Mississippi ou na Carolina do Sul, com seus emails e estados:

```
email | state
-------|-------
john.doe@gmail.com | MS
steven.jackson@hotmail.com | MS
mary.smith@yahoo.com | SC
```

* `select email, state, birth_date
from sales.customers
where (state = 'SC' or state = 'MS') and birth_date < '1991-12-28'`

> ```SELECT email, state, birth_date
FROM sales.customers
WHERE (state = 'SC' OR state = 'MS') AND birth_date < '1991-12-28';```

A saída será uma lista de todos os clientes no Mississippi ou na Carolina do Sul que nasceram antes de 28 de dezembro de 1991, com seus emails, estados e datas de nascimento:

```
email | state | birth_date
-------|-------|------------
john.doe@gmail.com | MS | 1980-01-01
steven.jackson@hotmail.com | MS | 1982-03-03
```

