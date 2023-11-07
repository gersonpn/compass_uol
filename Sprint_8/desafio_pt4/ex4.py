from pyspark.sql import SparkSession
from pyspark.sql.functions import rand, expr, when

spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False)

df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

df_nomes = df_nomes.withColumn("Escolaridade", expr("CASE WHEN rand() <= 0.33 THEN 'Fundamental' WHEN rand() <= 0.66 THEN 'Médio' ELSE 'Superior' END"))

df_nomes = df_nomes.withColumn("Pais", expr("array('Brasil', 'Argentina', 'Chile', 'Colômbia', 'Peru', 'Equador', 'Bolívia', 'Venezuela', 'Paraguai', 'Uruguai', 'Guiana', 'Suriname', 'Guiana Francesa')[(cast(rand() * 13 as int) + 1)]"))

df_nomes = df_nomes.withColumn("AnoNascimento", expr("cast(rand() * (2010 - 1945) + 1945 as int)"))

df_select = df_nomes.filter(df_nomes.AnoNascimento >= 2000).select("Nomes")
df_select.show(10, truncate=False)

df_nomes.createOrReplaceTempView("pessoas")

millennials_count = spark.sql("SELECT COUNT(*) as Count FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994")
millennials_count.show()

geracao_count = spark.sql("""
    SELECT Pais,
           CASE
               WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
               WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
               WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
               WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z'
           END as Geração,
           COUNT(*) as Quantidade
    FROM pessoas
    GROUP BY Pais, Geração
    ORDER BY Pais, Geração
""")
geracao_count.show()
