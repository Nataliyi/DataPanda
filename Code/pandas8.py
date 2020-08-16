import pandas as pd
import numpy as np
from time import time


def reversator(value):
    """" every value will be inverted by letter"""
    return value[::-1]


movie = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/7181_10279_bundle_archive.zip', compression='zip')

genres = movie[['movie_title', 'genres']]
# for i in genres.columns:
#     print(i)
# for i in genres.values:
#     print(i)
# for row in genres.values:
#     for value in row:
#         print(value)
# for i, row in genres.iterrows():
#     print(row.map(reversator))
# for i, col in genres.iteritems():
#     print(col.map(reversator))

budget = movie[['budget', 'duration']]
budget.applymap(lambda x: x + 1)
# apply map for the whole dataframe

# print(budget.apply(np.mean, axis=0))
# print(budget.apply(lambda x: x + 1))
# print(budget.transform(lambda x: x + 1))
# print(budget.mean() + 2)
# print(budget.values)
# extract array of numpy
np.mean(budget['budget'].dropna().values)
# necessary to apply dropna() (delete name of columns) before using of numpy

df = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/iris.csv')

before = time()
df.apply('mean')
after = time()
print(after - before)

before = time()
df.mean(axis=0)
after = time()
print(after - before)
# the best in speed

before = time()
df.apply(np.mean)
after = time()
print(after - before)

before = time()
df.describe().loc['mean']
after = time()
print(after - before)

