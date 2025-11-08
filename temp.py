
import numpy as np
import pandas as pd
import os

# Construct the path to the data file in an OS-independent way
data_dir='data'
filename='Salary_with_genders.csv'
# Get the current working directory of the script
current_dir = os.getcwd()

# Construct the path to the data file
file_path = os.path.join(current_dir, data_dir, filename)

# Normalize the path to resolve '..' and get the absolute path
file_path = os.path.abspath(file_path)

df = pd.read_csv(file_path)
print(df)

# Lay mau ngau nhien 30
sample = df.sample(n=30)
# Tinh gia tri trung binh cua mau
mean_salary = sample['Salary'].mean()
print(f"Gia tri trung binh cua mau la: {mean_salary}")
