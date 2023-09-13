from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.master(
    "local[*]").appName("Exercicio Intro").getOrCreate()

caminho_arquivo = "D:/DEV/Data & Analytics - PB - AWS Compass UOL/Compass-UOL-PB/Sprint 8/Exercicios/Tarefa 3/nomes_aleatorios.txt"

df_nomes = spark.read.csv(caminho_arquivo, header=False,
                          inferSchema=True, sep='\t')
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")
df_nomes.printSchema()
df_nomes.show(10)

spark.stop()
