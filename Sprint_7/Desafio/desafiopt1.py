##import boto3
import csv
import datetime

aws_access_key_id = 'AKIAWTKJODDH2EKYX5OF'
aws_secret_access_key ='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'
bucket_name = 'seriesefilmes'

# Configuração do cliente S3
#s3 = boto3.client('s3', aws_access_key_id = aws_access_key_id, aws_secret_access_key = aws_secret_access_key)

# Define os caminhos dos arquivos CSV de filmes e séries
csv_movies_path = '/app/movies.csv'
csv_series_path = '/app/series.csv'

# Define o nome do bucket S3 e os diretórios de destino
s3_bucket = 'seriesefilmes'
storage_layer = 'Raw'
data_source = 'Local'
data_format = 'CSV'
data_specification = 'Movies'
processing_date = datetime.datetime.now().strftime('%Y/%m/%d')

# Função para fazer o upload para o S3
def upload_to_s3(source_file, s3_path):
    s3.upload_file(source_file, s3_bucket, s3_path)

# Define os caminhos de destino no S3
s3_movies_path = f'{s3_bucket}/{storage_layer}/{data_source}/{data_format}/{data_specification}/{processing_date}/movies.csv'
s3_series_path = f'{s3_bucket}/{storage_layer}/{data_source}/{data_format}/{data_specification}/{processing_date}/series.csv'

# Upload dos arquivos para o S3
upload_to_s3(csv_movies_path, s3_movies_path)
upload_to_s3(csv_series_path, s3_series_path)

print(f'Arquivos CSV enviados para o S3: {s3_movies_path} e {s3_series_path}')
