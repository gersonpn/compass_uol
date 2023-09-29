# Crescimento Exponencial de Dados de Negócios

Há três classificações amplas de tipos de origem dos dados:

| Tipo de Dado       | Descrição                                             |
|---------------------|-------------------------------------------------------|
| Dados Estruturados  | Organizados em linhas e colunas de uma tabela.       |
| Dados Semiestruturados | Armazenados em conjuntos de pares de chave-valor. |
| Dados Não Estruturados | Não têm uma estrutura consistente.               |

Na AWS, o Amazon Simple Storage Service (Amazon S3) é o melhor lugar para armazenar todos os seus dados semiestruturados e não estruturados.

## Amazon Simple Storage Service (Amazon S3)

Amazon S3 é um serviço de armazenamento da AWS que permite armazenar objetos. Um objeto é composto por um arquivo e quaisquer metadados que descrevam esse arquivo. Para armazenar um objeto no Amazon S3, você faz o upload do arquivo que deseja armazenar no bucket. Ao fazer o upload de um arquivo, você pode definir permissões no objeto e adicionar metadados.

Buckets são contêineres lógicos para objetos. Você pode ter um ou mais buckets em sua conta e controlar o acesso a cada um individualmente. Você controla quem pode criar, excluir e listar objetos no bucket. Você também pode visualizar logs de acesso do bucket e seus objetos e escolher a região geográfica onde o Amazon S3 armazenará o bucket e o respectivo conteúdo.

Exemplo de URL para um objeto em um bucket chamado "doc" com a chave de objeto "2006-03-01/AmazonS3.html":

![Alt text](image-1.png)

Uma chave de objeto é um identificador exclusivo de um objeto em um bucket. Como a combinação de um bucket, chave e ID de versão identifica exclusivamente cada objeto, você pode considerar o Amazon S3 como um mapa de dados básico entre "bucket + chave + versão" e o próprio objeto.

## Data Lakes e Data Warehouses

Um data lake é um repositório centralizado que permite armazenar dados estruturados, semiestruturados e não estruturados em qualquer escala.

![Alt text](image-2.png)

Um data warehouse, por outro lado, é um repositório central de dados estruturados de várias origens. Os dados são transformados, agregados e preparados para relatórios e análises de negócios.

![Alt text](image-3.png)

### Data Marts

Para facilitar a análise, as organizações muitas vezes criam data marts, que são subconjuntos de dados de um data warehouse. Os data marts se concentram em um único assunto ou área funcional, permitindo análises mais específicas.

![Alt text](image-5.png)

## Armazenamento de Dados em Grande Escala

- Ao armazenar objetos individuais, recomenda-se o uso do Amazon S3.
- Para volumes massivos de dados semiestruturados e não estruturados, crie um data lake no Amazon S3.
- Para dados estruturados para análises complexas, armazene dados no Amazon Redshift.

## Apache Hadoop

O Apache Hadoop é um framework que facilita a análise de grandes quantidades de dados. Diferente dos sistemas tradicionais de bancos de dados, o Hadoop pode processar dados estruturados, semiestruturados ou não estruturados.

![Alt text](image-10.png)

O Hadoop usa uma arquitetura de processamento distribuído, o que permite a rápida análise de grandes volumes de dados.

### Implementação do Hadoop com o Amazon EMR

O Amazon EMR é o serviço AWS que implementa frameworks Hadoop. Ele permite a ingestão de dados de várias origens e armazena esses dados em um sistema de arquivos temporário, que pode ser o HDFS ou o EMRFS. Em seguida, a transformação e a análise dos dados são realizadas.

O Amazon EMRFS oferece uma alternativa ao HDFS, melhorando o desempenho ao eliminar a etapa de cópia de dados.

## Conclusão

Os data lakes e data warehouses têm suas próprias vantagens e são adequados para diferentes tipos de dados. A AWS fornece uma variedade de serviços para lidar com o armazenamento e processamento de dados em grande escala.

![Alt text](image-7.png)
