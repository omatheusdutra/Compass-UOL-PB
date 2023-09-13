# Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes.

import pandas as pd

csv_path = r'D:\DEV\Data & Analytics - PB - AWS Compass UOL\Compass-UOL-PB\Sprint 7\actors.csv'
data = pd.read_csv(csv_path)

most_movies_actor = data.loc[data['Number of Movies'].idxmax()]['Actor']
most_movies_count = data['Number of Movies'].max()

print("Ator ou atriz com maior número de filmes:", most_movies_actor)
print("Número de filmes:", most_movies_count)
