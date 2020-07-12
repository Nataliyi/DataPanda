import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib
from sklearn import tree
from sklearn.model_selection import train_test_split, cross_val_score

cd_data = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/dogs_n_cats.csv')
X_test = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/dogs_n_cats.csv').drop(['Вид', 'Высота', 'Шерстист'], axis=1)
X_train = pd.read_json('C:/Users/ediga/Projects/Python_Ln/Data/Files/dataset_209691_15 (1).txt').drop(['Высота', 'Шерстист'], axis=1)
y_test = cd_data.Вид
clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=1)
clf.fit(X_test, y_test)
tree.plot_tree(clf.fit(X_test, y_test), feature_names=list(X_test), filled=True)
print(clf.score(X_test, y_test))
print(np.unique(clf.predict(X_train), return_counts=True))
# просто посмотрим, сколько значений котиков и собачек в нашем предсказанном значении

