from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col, array_contains, split

try:
    # Inicializando o GlueContext
    sc = SparkContext()
    glueContext = GlueContext(sc)

    # Lendo os dados da tabela criada pelo crawler
    dynamic_frame = glueContext.create_dynamic_frame.from_catalog(database="sprint9", table_name="filmes_parquet")

    # Convertendo o DynamicFrame para um DataFrame
    dataframe = dynamic_frame.toDF()

    # Tratamento de valores nulos e filtragem
    dataframe = dataframe.withColumn("genero", split(col("genero"), ","))
    dataframe = dataframe.na.drop(subset=["generoArtista", "personagem", "nomeArtista", "anoNascimento","anoFalecimento", "profissao", "titulosMaisConhecidos"])

    # Filtrando os filmes de gênero Comedy e Animation
    dataframe = dataframe.filter(array_contains(col("genero"), "Comedy") | array_contains(col("genero"), "Animation"))

    # Criando as tabelas de dimensões e a tabela de fatos
    dimensao_artista = dataframe.select("id", "nomeArtista", "anoNascimento", "anoFalecimento", "profissao")
    dimensao_filme = dataframe.select("id", "titulopincipal", "titulooriginal", "anolancamento", "tempominutos", "genero")
    fatos_filmes = dataframe.select("id", "notamedia", "numerovotos")

    # Escrevendo os dados nas tabelas correspondentes na camada Refined

    # Lendo os dados da tabela criada pelo crawler
    dynamic_frame_api = glueContext.create_dynamic_frame.from_catalog(database="sprint9", table_name="2023_10_25")

    # Convertendo o DynamicFrame para um DataFrame
    dataframe_api = dynamic_frame_api.toDF()

    # Tratamento de valores nulos e filtragem
    dataframe_api = dataframe_api.na.drop(subset=["budget", "revenue"])
    dataframe_api = dataframe_api.filter((col("budget") != 0) & (col("revenue") != 0))

    # Criando as tabelas de dimensões e a tabela de fatos
    dim_artista = dataframe_api.select("id")
    dim_filme = dataframe_api.select("id", "title", "release_date")
    fato_filmes = dataframe_api.select("id", "budget", "revenue", "vote_average", "vote_count")

    # Escrevendo os dados nas tabelas correspondentes na camada Refined

    dimensao_artista.write.parquet("s3://seriesefilmes/seriesefilmes/refined/CSVdim_artista")
    dimensao_filme.write.parquet("s3://seriesefilmes/seriesefilmes/refined/CSVdim_filme")
    fatos_filmes.write.parquet("s3://seriesefilmes/seriesefilmes/refined/CSVfato_filmes")

    dim_artista.write.parquet("s3://seriesefilmes/seriesefilmes/refined/refined/api_dim_artista")
    dim_filme.write.parquet("s3://seriesefilmes/seriesefilmes/refined/api_dim_filme")
    fato_filmes.write.parquet("s3://seriesefilmes/seriesefilmes/refined/api_fato_filmes")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
