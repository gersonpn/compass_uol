# Use uma imagem oficial do Python como imagem pai
FROM python:3.7

# Instale as dependências do seu projeto
RUN pip install pandas

# Copie seu código-fonte para o contêiner
COPY . /app

# Defina o diretório de trabalho
WORKDIR /app

# Comando para executar o seu script
CMD ["python", "ex1.py"]
