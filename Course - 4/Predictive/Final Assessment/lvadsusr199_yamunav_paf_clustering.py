# -*- coding: utf-8 -*-
"""LVADSUSR199_YamunaV_PAF_Clustering.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mXFe7NKoKxtGrJqJ3iIwwkDtoXVEIZdo
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
from sklearn.metrics import silhouette_score

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv("/content/drive/MyDrive/PA_Final_today/customer_segmentation.csv")

df.head()

df.columns

df.shape

df.info()

df.describe(include='all').T

df.isnull().sum()

df['Income'] = df['Income'].fillna(df['Income'].mean())

df.isnull().sum()

df.duplicated().sum()

num_cols = df.select_dtypes(include=["int64","float64"]).columns
cor_mat = df[num_cols].corr()
plt.figure(figsize = (20,15))
sns.heatmap(cor_mat, annot =True, fmt = ".2f")
plt.show()

df.columns

df = df.drop(columns = ['ID','Year_Birth','Complain', 'Z_CostContact', 'Z_Revenue','Recency'])

import warnings
warnings.filterwarnings("ignore")

sse =[]
kr = range(1,11)
for k in kr:
  km = KMeans(n_clusters = k)
  km.fit(df[['NumWebVisitsMonth','NumStorePurchases']])
  sse.append(km.inertia_)

plt.xlabel('k')
plt.ylabel('sum of squared error')
plt.plot(kr,sse)

km = KMeans(n_clusters = 4)
silhouette_score(df[['NumWebVisitsMonth','NumStorePurchases']],km.fit_predict(df[['NumWebVisitsMonth','NumStorePurchases']]))

silhouette_score(df[['NumStorePurchases','Income']],km.fit_predict(df[['NumWebVisitsMonth','NumStorePurchases']]))

scaler = StandardScaler()
df['NumWebVisitsMonth'] = scaler.fit_transform(df[['NumWebVisitsMonth']])
df['NumStorePurchases'] = scaler.fit_transform(df[['NumStorePurchases']])

pred1 = km.fit_predict(df[['NumWebVisitsMonth','NumStorePurchases']])
df['cluster'] = pred1
print(km.cluster_centers_)

df.head()

df1 = df[df['cluster'] == 0]
df2 = df[df['cluster'] == 1]
df3 = df[df['cluster'] == 2]
df4 = df[df['cluster'] == 3]
plt.scatter(df1['NumWebVisitsMonth'],df1['NumStorePurchases'],color="red")
plt.scatter(df2['NumWebVisitsMonth'],df2['NumStorePurchases'],color="blue")
plt.scatter(df3['NumWebVisitsMonth'],df3['NumStorePurchases'],color="green")
plt.scatter(df4['NumWebVisitsMonth'],df4['NumStorePurchases'],color="yellow")
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color="purple",marker = "*",label="centroid")
plt.legend()
plt.show()