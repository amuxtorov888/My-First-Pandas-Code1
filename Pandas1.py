import pandas as pd

data = [100,102,104,200,202]

#series = pd.Series(data, index= ['apartment #1','apartment #2','apartment #3','apartment #4','apartment #5'])

series = pd.Series(data, index=['a','b','c','d','e'])

series.loc['c'] = 105

print(series)
print(series.loc['d'])

print(series.iloc[2])

print(series[series < 200])

