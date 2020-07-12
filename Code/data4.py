import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib
from sklearn import tree
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import f1_score, precision_score, recall_score

songs_data = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/songs.csv')
X = songs_data.drop(['year', 'artist', 'lyrics', 'song'], axis=1)
X = pd.get_dummies(X)  # классная штука, заменяет значения, где возможно на 1 и 0
y = songs_data.artist
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
clf = tree.DecisionTreeClassifier(max_depth=5)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)  # предсказание!
precision = precision_score(y_test, predictions, average='micro')


# depth = 1
# while True:
#     clf = DecisionTreeClassifier(criterion='entropy', max_depth=depth)
#     clf.fit(x_train, y_train)
#     predictions = clf.predict(x_test)
#     precision = precision_score(y_test, predictions, average='micro')
#     if precision > 0.78:
#         break
#     else:
#         depth += 1
