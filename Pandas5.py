import pandas as pd

df = pd.read_csv('data.csv', index_col='Name')

pokemon = input("Enter the name of a Pokemon: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f'{pokemon} not found in the dataset.')