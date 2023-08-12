# Big Data, Data Analytics e Armazenamento

## Big Data

**Resumo:** Big Data refere-se ao processamento e análise de conjuntos de dados extremamente grandes e complexos que ultrapassam a capacidade de ferramentas tradicionais de gerenciamento.

### Volume

Lida com grandes quantidades de dados, por exemplo:
- Sensores de IoT geram terabytes de dados por dia.

### Variedade

Envolve diversos tipos de dados (estruturados, não estruturados, semi-estruturados), por exemplo:
- Texto, imagens, vídeos e logs.

### Velocidade

Processa dados em tempo real ou próximo disso, por exemplo:
- Redes sociais geram dados em tempo real, como tweets.

### Veracidade

Lida com a qualidade e confiabilidade dos dados, por exemplo:
- Dados de diferentes fontes podem ter diferentes graus de precisão.

## Diferença entre Big Data e Ciência de Dados

- **Big Data:** Trata do processamento de grandes volumes de dados.
- **Ciência de Dados:** Envolve análise, modelagem e interpretação de dados para obter insights.

## Big Data Analytics

Refere-se ao processo de análise de grandes conjuntos de dados para descobrir padrões, tendências e insights valiosos.

## Bancos de Dados Relacionais e Não Relacionais

### Bancos de Dados Relacionais

Utilizados para armazenar dados estruturados em tabelas com esquemas fixos, por exemplo:
- MySQL
- PostgreSQL

### Bancos de Dados Não Relacionais

Flexíveis para dados variados e não possuem um esquema rígido, por exemplo:
- MongoDB (documentos)
- Cassandra (colunas)
- Neo4j (grafos)

## Data Lake, Data Store e Data Warehouse

### Data Lake

Armazena dados brutos e variados, como um grande repositório, por exemplo:
- Amazon S3

### Data Store

Armazena dados estruturados para recuperação rápida, por exemplo:
- Amazon DynamoDB

### Data Warehouse

Armazena dados processados e preparados para análise, por exemplo:
- Google BigQuery

## Sistema Híbrido de Armazenamento

Combina armazenamento local e em nuvem para otimizar custo e desempenho, por exemplo:
- Azure Hybrid Storage

## Cluster, Escalabilidade Horizontal e Armazenamento Paralelo

### Cluster

Grupo de computadores interconectados para processamento conjunto, por exemplo:
- Kubernetes

### Escalabilidade Horizontal

Adicionar mais máquinas para aumentar a capacidade, por exemplo:
- Amazon EC2 Auto Scaling

### Armazenamento Paralelo

Dividir dados para processamento simultâneo, por exemplo:
- Hadoop Distributed File System (HDFS)

## Apache Hadoop e HDFS

### Apache Hadoop

Framework para processamento distribuído de Big Data, por exemplo:
- Amazon EMR
- Google Dataproc

### HDFS (Hadoop Distributed File System)

Sistema de arquivos distribuído para armazenar dados no Hadoop. Segmenta arquivos em blocos para distribuição.

## Computação em Nuvem e Serviços Principais

### Computação em Nuvem

Fornecimento de recursos de TI via internet, exemplos de serviços principais:

- Amazon Web Services (AWS)
  - EC2 (máquinas virtuais)
  - S3 (armazenamento)
  - Redshift (data warehouse)

- Microsoft Azure
  - Virtual Machines
  - Azure Blob Storage
  - Azure SQL Data Warehouse

- Google Cloud Platform (GCP)
  - Google Compute Engine
  - Cloud Storage
  - BigQuery

## MLOps, DataOps e AIOps

### MLOps

Práticas para gerenciar o ciclo de vida de soluções de Machine Learning, por exemplo:
- Azure Machine Learning

### DataOps

Abordagem colaborativa para melhorar a qualidade e automação dos dados, por exemplo:
- Delta Lake

### AIOps

Uso de IA e Machine Learning para operações de TI, por exemplo:
- IBM Watson AIOps

## Data as a Service (DaaS)

Oferece acesso a conjuntos de dados sem a necessidade de armazenamento local, por exemplo:
- AWS Data Exchange

## Diferença entre Big Data e Small Data

**Big Data:** Lida com conjuntos de dados massivos, requerendo abordagens especiais.

**Small Data:** Dados em volumes menores, mais tradicionais.

## Data Mesh

Estratégia para gerenciar dados de forma distribuída e escalável, focando em domínios específicos, por exemplo:
- Zalando's Data Mesh

## ETL e ELT

### ETL (Extração, Transformação e Carregamento)

Movimenta dados de fontes para um destino após a transformação, por exemplo:
- Apache NiFi

### ELT (Extração, Carregamento e Transformação)

Os dados são primeiro carregados e a transformação ocorre após, por exemplo:
- Talend

## ETL e ELT em Computação em Nuvem

Em nuvem, os dados frequentemente são carregados antes de serem transformados devido à escalabilidade dos serviços, por exemplo:
- AWS Glue (ETL)
- Google Cloud Dataflow (ELT)

## Criando um Projeto Big Data

1. **Business Case:** Identifique os objetivos de negócios e problemas a resolver, por exemplo:
   - Otimizar processos de atendimento ao cliente.

2. **Planejamento de Produto:** Defina as etapas e recursos necessários, por exemplo:
   - Escolher as tecnologias a serem usadas e as equipes envolvidas.

3. **Definição de Requisitos:** Especifique as necessidades técnicas e funcionais, por exemplo:
   - Integrar fontes de dados e definir formatos.

4. **Criação de um Total Business Value Assessment:** Avalie o valor total do projeto para a organização, por exemplo:
   - Estimar o retorno financeiro, melhoria operacional ou insights obtidos.

