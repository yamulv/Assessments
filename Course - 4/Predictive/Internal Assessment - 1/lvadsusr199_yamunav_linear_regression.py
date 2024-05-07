# -*- coding: utf-8 -*-
"""LVADSUSR199_YamunaV_Linear_Regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mj7XGgR4B28zS6OIXCuWspI5Cm_ZPsdX
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_squared_error

from google.colab import drive
drive.mount('/content/drive')

df =  pd.read_csv("/content/expenses.csv")

df.head()

df.info()

df.describe(include='all')

df.shape

df.columns

#1
df.isnull().sum()

df['bmi']=df['bmi'].fillna(df['bmi'].mean())

df.isnull().sum()

for column in df.select_dtypes(include=["int64","float64"]).columns:
  q1 = df[column].quantile(0.25)
  q3 = df[column].quantile(0.75)
  iqr = q3 - q1
  l = q1 - 1.5 * iqr
  u = q3 + 1.5 * iqr
  df[column] = df[column].clip(lower=l,upper=u)
  sns.boxplot(x=df[column])
  plt.title(f'boxplot of {column}')
  plt.show()

#2
from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()

for column in df.select_dtypes(include= "object").columns:
  df[column] = label_encoder.fit_transform(df[column])

df.head()

#3
num_col = df.select_dtypes(include=["int64","float64"]).columns
corr = df[num_col].corr()
plt.figure(figsize=(8,5))
sns.heatmap(corr, annot =True, fmt= ".2f", cmap="coolwarm")
plt.title("Correlation matrix")
plt.show()

df.duplicated().sum()

df = df.drop_duplicates()

df.duplicated().sum()

#4
X = df.drop(columns = ["charges"])
y = df["charges"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size= 0.3, random_state = 42)

#5
model = LinearRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)

#6
print("r2_score: ",r2_score(y_test, pred))
print("rmse: ",mean_squared_error(y_test, pred,squared=False))
print("mse: ",mean_squared_error(y_test, pred))