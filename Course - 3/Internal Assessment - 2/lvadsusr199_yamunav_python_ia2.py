# -*- coding: utf-8 -*-
"""LVADSUSR199_YamunaV_Python_IA2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zh6jddlonppC_Ib1rZd1mkXaaj0gX86u
"""

import numpy as np

#Question 1
arr1 = np.array([1,2,3,4,5])
print(arr1)
minv = np.min(arr1)
print("min:", minv)
maxv = np.max(arr1)
print("max:",maxv)
sumv = np.sum(arr1)
print("sum:",sumv)
meanv = np.mean(arr1)
print("mean:",meanv)
stdv = np.std(arr1)
print("std:",stdv)

#Question 2
health_data = np.array([[160, 70, 30],   # height, weight, age for individual 1
                        [165, 65, 35],   # height, weight, age for individual 2
                        [170, 75, 40]])  # height, weight, age for individual 3

mean1 = np.mean(health_data)
print("mean:",mean1)
std1 = np.std(health_data)
print("std:",std1)

x=health_data[0:]
y=health_data[1:]
z=health_data[2:]
print(x)

c_xy = np.corrcoef(x,y)
print("Correlation(1,2): \n",c_xy)

c_yz = np.corrcoef(y,z)
print("Correlation(2,3): \n",c_yz)

c_zx = np.corrcoef(z,x)
print("Correlation(3,1): \n",c_zx)

#Question 3
student = np.array([[30,40,50,60],[50,20,40,80]])
print(student)
s1 = student[0,1:]
s2 = student[1,1:]
student1_avg = (s1.sum())/3
print("student1_avg: ", student1_avg)
student2_avg = (s2.sum())/3
print("student2_avg: ", student2_avg)

#Question 4
temp_readings = np.linspace(15,25,24)
print("Temperature readings", temp_readings)

#Question 5
daily_closing_prices = np.array([100, 102, 98, 105, 107, 110, 108, 112, 115, 118, 120])
daily_closing_price = np.array([100, 102, 98, 105, 107, 110, 108, 112, 115, 118, 120,0,0,0,0])
window_size = 5
arrx = np.array_split(daily_closing_price,3)
print(arrx)
arra = np.array([100, 102,  98, 105, 107])
arrb = np.array([110, 108, 112, 115, 118])
arrc =np.array([120,   0,   0,   0,   0])
print("Frist 5 days:",np.mean(arra))
print("Second 5 days:",np.mean(arrb))
print("Next 5 days:",np.mean(arrc))

#Question 6
import random
synthetic_data = np.random.rand(1,100)
print(synthetic_data)

#Question 7
properties_matrix = np.array([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]])
if True:
  print(np.unique(properties_matrix))
  print("Since values are unique\n")
  print("Determinant = 1")

#Question 8
arr_3d = np.array([[[1,2,7]]])
print("Dimension:",arr_3d.ndim)
result = arr_3d[arr_3d > 5]
print(result)

#Question 9
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
        'Age': [25, 30, 35, 40, 45, 50, 55],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Miami', 'Boston'],
        'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales', 'IT', 'HR']}

df = pd.DataFrame(data)
print(df)

#Question 10
data = {'Department': ['Electronics', 'Electronics', 'Clothing', 'Clothing', 'Home Goods'],
        'Salesperson': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Sales': [70000, 50000, 30000, 40000, 60000]}

df1 = pd.DataFrame(data)
print(df1)

a = df1.groupby('Department')['Sales'].aggregate('mean')
print(a)

#Question 11
data = {
    'Product': ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries', 'Flour', 'Grapes'],
    'Category': ['Fruit', 'Fruit', 'Fruit', 'Fruit', 'Fruit', 'Bakery', 'Fruit'],
    'Price': [1.20, 0.50, 3.00, 2.50, 4.00, 1.50, 2.00],
    'Promotion': [True, False, True, True, False, True, False]
}

xdf = pd.DataFrame(data)
print(xdf)
avg = xdf['Price'].mean()
print("Avg:", avg)
dc = xdf.groupby('Category')['Price'].aggregate('mean')
print(dc)
f = xdf.groupby('Product')['Price'].aggregate('mean')
print(f)

#Question 12
employee_data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department': ['HR', 'IT', 'Finance', 'IT'],
    'Manager': ['John', 'Rachel', 'Emily', 'Rachel']
}

# Dataset of employee project assignments
project_data = {
    'Employee': ['Alice', 'Charlie', 'Eve'],
    'Project': ['P1', 'P3', 'P2']
}

employee = pd.Series(['Alice', 'Charlie', 'Eve'])
project = pd.Series(['P1', 'P3', 'P2'])

print(employee_data)
employee_data = pd.DataFrame(project_data)
print(employee_data)

#Question 13
Q13 = pd.read_csv("/content/drive/MyDrive/PY_IA2/Q13_sports_team_stats.csv")
print(Q13)
print(Q13.groupby('TeamID')['GamesPlayed'].aggregate('mean'))
print(Q13.groupby('TeamID')['Wins'].aggregate('mean'))

#Question 14
Q14 = pd.read_csv("/content/drive/MyDrive/PY_IA2/Q14_customer_purchases.csv")
print(Q14)

print(Q14.groupby('CustomerID')['PurchaseAmount'].aggregate('mean'))

#Question 15
Q15 = pd.read_csv("/content/drive/MyDrive/PY_IA2/Q15_student_grades.csv")
print(Q15)

print(Q15.groupby('Subject')['Grade'].aggregate('mean'))