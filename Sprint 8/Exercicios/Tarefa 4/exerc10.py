from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, lit, rand

spark = SparkSession.builder.master(
    "local[*]").appName("Exercicio Intro").getOrCreate()

caminho_arquivo = "D:/DEV/Data & Analytics - PB - AWS Compass UOL/Compass-UOL-PB/Sprint 8/Exercicios/Tarefa 3/nomes_aleatorios.txt"

df_nomes = spark.read.csv(caminho_arquivo, header=False,
                          inferSchema=True, sep='\t')
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")
df_nomes = df_nomes.withColumn(
    "AnoNascimento", (1945 + (rand() * 66)).cast("int"))

paises = ["Brasil", "Argentina", "Chile", "Colômbia", "Uruguai", "Paraguai",
          "Bolívia", "Peru", "Equador", "Venezuela", "Suriname", "Guiana", "Guiana Francesa"]
df_nomes = df_nomes.withColumn("Pais", when(
    col("AnoNascimento") <= 1980, lit(paises[0])).otherwise(lit(paises[1])))

df_nomes.createOrReplaceTempView("pessoas")

consulta_bb = "SELECT Pais, COUNT(*) AS Quantidade, 'Baby Boomers' AS Geracao FROM pessoas WHERE AnoNascimento BETWEEN 1944 AND 1964 GROUP BY Pais"
consulta_gen_x = "SELECT Pais, COUNT(*) AS Quantidade, 'Geração X' AS Geracao FROM pessoas WHERE AnoNascimento BETWEEN 1965 AND 1979 GROUP BY Pais"
consulta_millennials = "SELECT Pais, COUNT(*) AS Quantidade, 'Millennials' AS Geracao FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994 GROUP BY Pais"
consulta_gen_z = "SELECT Pais, COUNT(*) AS Quantidade, 'Geração Z' AS Geracao FROM pessoas WHERE AnoNascimento BETWEEN 1995 AND 2015 GROUP BY Pais"

df_bb = spark.sql(consulta_bb)
df_gen_x = spark.sql(consulta_gen_x)
df_millennials = spark.sql(consulta_millennials)
df_gen_z = spark.sql(consulta_gen_z)

df_resultado = df_bb.unionAll(df_gen_x).unionAll(
    df_millennials).unionAll(df_gen_z)

df_resultado = df_resultado.orderBy(
    col("Pais"), col("Geracao"), col("Quantidade"))

df_resultado.show(df_resultado.count(), truncate=False)

spark.stop()
