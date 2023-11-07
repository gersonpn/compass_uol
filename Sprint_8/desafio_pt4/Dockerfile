# Use a imagem base do Ubuntu 20.04
FROM ubuntu:20.04

# Atualize o sistema e instale as dependências
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk wget && \
    apt-get clean

# Define a variável de ambiente JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

# Faça o download do Apache Spark
WORKDIR /opt
RUN wget -q https://archive.apache.org/dist/spark/spark-3.0.3/spark-3.0.3-bin-hadoop3.2.tgz && \
    tar -xzf spark-3.0.3-bin-hadoop3.2.tgz && \
    rm spark-3.0.3-bin-hadoop3.2.tgz && \
    mv spark-3.0.3-bin-hadoop3.2 spark

# Define as variáveis de ambiente do Spark
ENV SPARK_HOME /opt/spark
ENV PATH $SPARK_HOME/bin:$PATH

# Define a porta Spark para acesso à interface web
EXPOSE 4040

# Inicie o Spark Master por padrão
CMD ["spark-class", "org.apache.spark.deploy.master.Master"]
