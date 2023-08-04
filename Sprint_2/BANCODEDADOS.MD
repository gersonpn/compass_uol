# SPRINT 2

## SQL para Análise de Dados: Do básico ao avançado



```sql
-- select email from sales.customers

This query will select the `email` column from the `sales.customers` table.

```

**Example:**

```sql
email
-------
john.doe@example.com
jane.doe@example.com
```

```sql
-- select email, first_name, last_name from sales.customers

This query will select the `email`, `first_name`, and `last_name` columns from the `sales.customers` table.

```

**Example:**

```sql
email | first_name | last_name
------- | -------- | --------
john.doe@example.com | John | Doe
jane.doe@example.com | Jane | Doe
```

```sql
-- todas as colunas da tabela

-- select * from sales.customers

This query will select all columns from the `sales.customers` table.

```

**Example:**

```sql
email | first_name | last_name | state | birth_date
------- | -------- | -------- | -------- | --------
john.doe@example.com | John | Doe | MS | 1980-01-01
jane.doe@example.com | Jane | Doe | SC | 1991-12-28
```

```sql
-- Distinct, remove linhas duplicadas

-- select brand from sales.products

This query will select the `brand` column from the `sales.products` table. There may be duplicate brands in the table, so this query will return one row for each unique brand.

```

**Example:**

```sql
brand
-------
Apple
Samsung
Google
```

```sql
-- select distinct brand from sales.products

This query will select the `brand` column from the `sales.products` table, but it will only return one row for each unique brand. This is the same as the previous query, but it uses the `distinct` keyword to remove duplicate rows.

```

**Example:**

```sql
brand
-------
Apple
Samsung
Google
```

```sql
-- select distinct brand,model_year from sales.products

This query will select the `brand` and `model_year` columns from the `sales.products` table, but it will only return one row for each unique combination of brand and model year.

```

**Example:**

```sql
brand | model_year
------- | --------
Apple | 2022
Apple | 2023
Samsung | 2022
Samsung | 2023
Google | 2022
Google | 2023
```

```sql
-- select email state from sales.customers where state = 'MS'

This query will select the `email` and `state` columns from the `sales.customers` table where the `state` column is equal to `MS`.

```

**Example:**

```sql
email | state
------- | --------
john.doe@example.com | MS
```

```sql
-- select email state from sales.customers where state = 'SC' or state = 'MS'

This query will select the `email` and `state` columns from the `sales.customers` table where the `state` column is equal to `SC` or `MS`.

```

**Example:**

```sql
email | state
------- | --------
john.doe@example.com | MS
jane.doe@example.com | SC
```

```sql
select email, state, birth_date
from sales.customers
where (state = 'SC' or state = 'MS') and birth_date < '1991-12-28'

This query will select the `email`, `state`, and `birth_date` columns from the `sales.customers` table where the `state` column is equal to `SC` or `MS` and the `birth_date` column is less than `1991-12-28`.

```

**Example:**

```sql
email | state | birth_date
------- | -------- | --------
jane.doe@example.com | SC | 1991-01-01
```