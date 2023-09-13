from pyspark.sql import SparkSession
from pyspark.sql.functions import col, rand, when

spark = SparkSession.builder.master(
    "local[*]").appName("Exercicio Intro").getOrCreate()

caminho_arquivo = "D:/DEV/Data & Analytics - PB - AWS Compass UOL/Compass-UOL-PB/Sprint 8/Exercicios/Tarefa 3/nomes_aleatorios.txt"

df_nomes = spark.read.csv(caminho_arquivo, header=False,
                          inferSchema=True, sep='\t')
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

paises_americadosul = ["Argentina", "Bolívia", "Brasil", "Chile", "Colômbia",
                       "Equador", "Guiana", "Paraguai", "Peru", "Suriname", "Uruguai", "Venezuela"]

df_nomes = df_nomes.withColumn("Pais", when(rand() <= 0.083, "Argentina")
                               .when(rand() <= 0.166, "Bolívia")
                               .when(rand() <= 0.249, "Brasil")
                               .when(rand() <= 0.332, "Chile")
                               .when(rand() <= 0.415, "Colômbia")
                               .when(rand() <= 0.498, "Equador")
                               .when(rand() <= 0.581, "Guiana")
                               .when(rand() <= 0.664, "Paraguai")
                               .when(rand() <= 0.747, "Peru")
                               .when(rand() <= 0.830, "Suriname")
                               .when(rand() <= 0.913, "Uruguai")
                               .otherwise("Venezuela"))
df_nomes.printSchema()
df_nomes.show(10)

spark.stop()
