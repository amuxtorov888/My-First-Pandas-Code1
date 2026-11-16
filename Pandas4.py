# pyright: reportMissingModuleSource=false
import pandas as pd


df = pd.read_csv('data.csv', index_col='Name')


#print(df['Height'].to_string()) 
#print(df['Weight'].to_string())
#print(df[['Name', 'Weight', 'Height']].to_string())

#print(df['Height'] + df['Weight'])
#print(df['Height'] * df['Weight'])
#print(df['Height'] / df['Weight'])

#print(df.loc['Pikachu'])
#print(df.loc['Charizard', ['Weight', 'Height']]) 
#print(df.loc['Charizard': 'Pikachu', ['Weight', 'Height']])
print(df.iloc[0:20:2, 0:3])
print(df.iloc[20:50:3,0:5])
