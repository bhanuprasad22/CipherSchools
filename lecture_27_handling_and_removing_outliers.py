# -*- coding: utf-8 -*-
"""Lecture 27 - Handling And Removing Outliers

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-6XyrbE3JbGLGtW70YLIlHgHDMZnjAGI
"""

import pandas as pd

# Load the dataset

df = pd.read_csv("Sample.csv")
print(df)

"""# Visualize Outliers using Boxplots"""

import matplotlib.pyplot as plt

# Boxplot to visulaize outliers int the Age column
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.boxplot(df['Age'].dropna())
plt.title('Boxplot of age')

# Boxplot to visualize outliers in the Salary column
plt.subplot(1,2,2)
plt.boxplot(df['Salary'].dropna())
plt.title('Boxplot of Salary')

plt.show()

"""# Handling outliers"""

# Capping the outliers using IQR method

df_capped = df.copy()
for column in ['Age','Salary']:
  Q1 = df_capped[column].quantile(0.25)
  Q3 = df_capped[column].quantile(0.75)
  IQR = Q3 - Q1
  lower_bound = Q1 - 1.5 * IQR
  upper_bound = Q3 + 1.5 * IQR
  df_capped[column] = df_capped[column].apply(lambda x: upper_bound if x > upper_bound else (lower_bound if x < lower_bound else x))

print("Data after capping outliers using IQR method: ")
print(df_capped)