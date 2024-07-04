# -*- coding: utf-8 -*-
"""Lecture 15 - Data Manipulation And Analysis With Numpy

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19aR1ix-I2GdxTjCkNteFLmtDPX--xUxk
"""

pip install numpy

import numpy as np

#Creating a 1D array from a list
arr1 = np.array([1,2,3,4,5])
print(arr1)

#Creating a 2D array from a list of lists
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)

"""# Creating Arrays with Functions"""

zeros = np.zeros((3,4))
print(zeros)

ones = np.ones((2,3))
print(ones)

# Creating an array with a range of values

range_arr = np.arange(10,20,2)
print(range_arr)

# Creating an array with random values

random_arr = np.random.rand(3, 3)
print(random_arr)

"""# Basic Array Operations - Element Wise Operations

"""

arr = np.array([1,2,3,4,5])

# Element-wise operations
print(arr + 2)
print(arr * 2)
print(arr - 1)
print(arr / 2)

arr = np.array([1,2,3,4,5])

print(np.sqrt(arr))
print(np.exp(arr))
print(np.log(arr))
print(np.sin(arr))

"""# Indexing and Slicing - Slicing"""

arr = np.array([1,2,3,4,5])

print(arr[1:4])
print(arr[:3])
print(arr[2:])

"""## Indexing and Slicing - Advanced Indexing"""

arr = np.array([1,2,3,4,5])

#Boolean indexing
print(arr[arr>3])

#Fancy indexing
indices = [0,2,4]
print(arr[indices])

"""# Reshaping and Transposing - Reshaping Arrays"""

arr = np.array([[1,2,3],[4,5,6]])
print(arr)

reshaped = arr.reshape((3,2))
print(reshaped)

"""# Reshaping and Transposing - Transposing Arrays"""

arr = np.array([[1,2,3],[4,5,6]])

transposed = arr.T
print(transposed)

"""# Aggregation Functions - Sum and Mean"""

arr = np.array([[1,2,3],[4,5,6]])

print(np.sum(arr))
print(np.sum(arr, axis=0)) #Sum along columns
print(np.sum(arr, axis=1)) #sum along rows
print(np.mean(arr)) #mean of all elements
print(np.argmin(arr)) #Index of minimum value
print(np.argmax(arr)) #Index of maximum value