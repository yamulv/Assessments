# -*- coding: utf-8 -*-
"""LVADSUSR199_YamunaV_PAF_Regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yBJ0U8nMFNnC9jdEHzn9iOeYBph9UOd6
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv("/content/drive/MyDrive/PA_Final_today/Fare prediction.csv")

df.head()

df.describe(include='all').T

df.info()

df.columns

df.shape

df.isnull().sum()

df.duplicated().sum()

num_cols = df.select_dtypes(include=["int64","float64"]).columns
cor_mat = df[num_cols].corr()
sns.heatmap(cor_mat, annot =True, fmt = ".2f")
plt.show()

for column in df.select_dtypes(include=["int64","float64"]).columns:
  sns.boxplot(x = df[column])
  plt.show()

#Removing outliner removes important datapoints
"""for column in df.select_dtypes(include=["int64","float64"]).columns:
  q1 = df[column].quantile(0.25)
  q3 = df[column].quantile(0.75)
  iqr = q3 - q1
  l = q1 - 1.5 * iqr
  u = q3 + 1.5 * iqr
  df[column] = df[column].clip(lower=l, upper=u)
  sns.boxplot(x = df[column])
  plt.show()"""

label_e = LabelEncoder()
for column in df.select_dtypes(include=["object"]).columns:
  df[column]= label_e.fit_transform(df[column])

df.head()

X = df.drop(columns=["key","fare_amount"])
y = df["fare_amount"]

X_train, X_test, y_train, y_test = train_test_split(  X,y, test_size = 0.3, random_state = 42)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

model_1 = LinearRegression()
model_1.fit(X_train_s,y_train)

pred_1 = model_1.predict(X_test_s)

print("r2 score:", r2_score(y_test,pred_1))
print("mse:", mean_squared_error(y_test,pred_1))
print("rmse:", mean_squared_error(y_test,pred_1, squared= False))
print("mae:", mean_absolute_error(y_test,pred_1))

model_2 = RandomForestRegressor()
model_2.fit(X_train_s,y_train)

pred_2 = model_2.predict(X_test_s)

print("r2 score:", r2_score(y_test,pred_2))
print("mse:", mean_squared_error(y_test,pred_2))
print("rmse:", mean_squared_error(y_test,pred_2, squared= False))
print("mae:", mean_absolute_error(y_test,pred_2))