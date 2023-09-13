# Apresente o nome do ator/atriz com a maior média por filme.

import pandas as pd

csv_path = r'D:\DEV\Data & Analytics - PB - AWS Compass UOL\Compass-UOL-PB\Sprint 7\actors.csv'

data = pd.read_csv(csv_path)
data['Average Gross per Movie'] = (
    data['Total Gross'] / data['Number of Movies']).round(2)

highest_average_actor = data.loc[data['Average Gross per Movie'].idxmax(
)]['Actor']
highest_average = data['Average Gross per Movie'].max()

print("Ator ou atriz com maior média por filme:", highest_average_actor)
print("Média por filme:", highest_average)
