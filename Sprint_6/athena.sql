WITH decadas as (

SELECT
SUBSTRING (CAST(ano as varchar), 1,3) || '0' as decada , nome, sum (total) as total
FROM
meubanco.meubanco
WHERE ano >= 1950

GROUP BY SUBSTRING (CAST(ano as varchar), 1,3) || '0', nome

ORDER BY total DESC

),

ranking as (
SELECT
nome,
decada,
total,

ROW_NUMBER () OVER (partition BY decada order by total DESC) as posicao

FROM
decadas


)


SELECT * FROM ranking WHERE posicao <= 3

ORDER BY decada, total desc

