
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 40, 45],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
    "Salary": [50000, 60000, 70000, 80000, 90000],
    "Department": ["HR", "Finance", "IT", "Marketing", "Sales"],
    "Experience": [2, 5, 8, 10, 12],
    "Education": ["Bachelor's", "Master's", "PhD", "Bachelor's", "Master's"],
    "Marital Status": ["Single", "Married", "Single", "Married", "Single"],
    "Gender": ["Female", "Male", "Male", "Male", "Female"]
}

# 2. DataFrame 
df = pd.DataFrame(
    data,
    index=['Employee1', 'Employee2', 'Employee3','Employee4', 'Employee5']
)

print("Third employee:")
print(df.iloc[2])


df['Bonus'] = [5000, 6000, 7000, 8000, 9000]

new_row = pd.DataFrame([
    {
        "Name": "Frank",
        "Age": 35,
        "City": "San Francisco",
        "Salary": 65000,
        "Department": "IT",
        "Experience": 6,
        "Education": "Master's",
        "Marital Status": "Single",
        "Gender": "Male",
        "Bonus": 6500
    },
    {
        "Name": "Akmal",
        "Age": 28,
        "City": "Chust",
        "Salary": 55000,
        "Department": "Programmer",
        "Experience": 4,
        "Education": "Bachelor's",
        "Marital Status": "Married",
        "Gender": "Male",
        "Bonus": 5500
    }
], index=['Employee6', 'Employee7'])

df = pd.concat([df, new_row])

figure, ax = plt.subplots(
    figsize=(12, 5),
    nrows=1,
    ncols=2
)

# Birinchi grafik: Salary histogrammasi
ax[0].hist(
    df['Salary'],
    bins=5,
    color='blue',
    alpha=0.7,
    edgecolor='black'
)

ax[0].set_title('Salary Distribution')
ax[0].set_xlabel('Salary')
ax[0].set_ylabel('Frequency')

# Ikkinchi grafik: Salary va Bonus scatter plot
ax[1].scatter(
    df['Salary'],
    df['Bonus'],
    color='red',
    marker='o',
    s=80
)

ax[1].set_title('Salary vs Bonus')
ax[1].set_xlabel('Salary')
ax[1].set_ylabel('Bonus')

# Grafiklarni tartibga keltirish
plt.tight_layout()
plt.show()

# 8. Yakuniy jadvalni chiqarish
print("\nComplete Employee Data:")
print(df)
