# Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.

import pandas as pd

csv_path = r'D:\DEV\Data & Analytics - PB - AWS Compass UOL\Compass-UOL-PB\Sprint 7\actors.csv'

data = pd.read_csv(csv_path)

movie_counts = data['#1 Movie'].value_counts()
max_frequency = movie_counts.max()
most_frequent_movies = movie_counts[movie_counts == max_frequency]

for movie, frequency in most_frequent_movies.items():
    print("Filme:", movie)
    print("Frequência:", frequency)
    print()
