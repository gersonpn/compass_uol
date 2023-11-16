import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
job.commit()

# leitura do CSV
filmes_df = spark.read.format("csv").option("header", "true").option("delimiter", "|").load("s3://seriesefilmes/seriesefilmes/Raw/Local/CSV/Movies/2023/10/25/movies.csv")

# formato Parquet
filmes_df.write.parquet("s3://seriesefilmes/seriesefilmes/trusted/filmes.parquet")


# arquivos json

filmes_json_base = 's3://seriesefilmes/seriesefilmes/Raw/Local/CSV/Movies/2023/10/25'


filmes_json = spark.read.json(f's3://seriesefilmes/seriesefilmes/Raw/Local/CSV/Movies/2023/10/25/*.json')

# Extraindo a data completa do caminho do arquivo
date = '-'.join(filmes_json_base.split('/')[-3:])

# Adicionando a coluna 'dt' ao DataFrame
filmes_json_df = filmes_json.withColumn("dt", lit(date))


# Escrevendo os dados JSON transformados na Trusted Zone no formato PARQUET
filmes_json.write.parquet(f"s3://seriesefilmes/seriesefilmes/trusted/{date}/filmes_json.parquet")

job.commit()