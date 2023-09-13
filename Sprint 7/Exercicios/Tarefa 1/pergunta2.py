# Apresente a média da coluna contendo o número de filmes.

import pandas as pd

csv_path = r'D:\DEV\Data & Analytics - PB - AWS Compass UOL\Compass-UOL-PB\Sprint 7\actors.csv'
data = pd.read_csv(csv_path)

average_movies = data['Number of Movies'].mean()

print("Média do número de filmes:", average_movies)
