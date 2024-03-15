import pandas as pd

data = pd.read_csv('res_dpre.csv')


insight_1 = "Insight 1: Mean value of column rating is {0}".format(data['rating'].mean())
with open('eda-in-1.txt', 'w') as file:
    file.write(insight_1)


insight_2 = "Insight 2: Maximum value in column discounted_price is {0}".format(data['discounted_price'].max())
with open('eda-in-2.txt', 'w') as file:
    file.write(insight_2)


insight_3 = "Insight 3: Number of unique categories in column category is {0}".format(data['category'].nunique())
with open('eda-in-3.txt', 'w') as file:
    file.write(insight_3)
