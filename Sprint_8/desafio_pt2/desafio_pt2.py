import requests
import pandas as pd
import boto3
import json

def lambda_handler(event, context):
  s3 = boto3.client('s3')
  api_key = "b3d7b7c704e47368d2e7339f38e95606"
  bucket_name = "seriesefilmes"
  remote_directory_path = "seriesefilmes/Raw/Local/CSV/Movies/2023/10/25/"
  bucket_movie = 'seriesefilmes/Raw/Local/CSV/Movies/2023/10/25/movies.csv'
  movies_file = s3.get_object(Bucket=bucket_name, Key=bucket_movie)


  dataframe = pd.read_csv (movies_file['Body'], delimiter='|', dtype='unicode')
  filtered_df = dataframe[dataframe['genero'].str.contains(r'\bAnimation,Comedy\b', case=False, regex=True)]

    # obtendo os ids distintos
  id = filtered_df['id'].unique()
  id = list(id)
  dados = []
  n = 0
  
  for i in id:
    url_api = f"https://api.themoviedb.org/3/movie/{i}?api_key={api_key}&language=pt-BR"
    response = requests.get(url_api)
    print(response.status_code)
    if response.status_code == 200:
      dados.append(response.json())
    if len(dados) == 100:
      n += 1
      js = json.dumps(dados)
      s3.put_object(Bucket=bucket_name, Key=remote_directory_path+f'filme_{n}.json', Body=js)
      dados = []
  return {
          'statusCode': 200,
          'body': json.dumps('Hello from Lambda!')
      }