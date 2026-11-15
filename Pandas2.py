import pandas as pd

calories = {"Day1": 1750, "Day2": 2100, "Day3": 1700, "Day4": 2200, "Day5": 1800}

   

series = pd.Series(calories)

print(series)

#print(series.loc['Day3'])
#print(series.loc['Day3'] + 500)

#print(series[series >= 2000])
#print(series[series < 2000])

for i in calories:
    if calories[i] < 2000:
        print("You are under your calorie goal for", i)
    else:
        print("You are over your calorie goal for", i)
    
print("You have consumed", series.sum(), "calories in total this week")   
