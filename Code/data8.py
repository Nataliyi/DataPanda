import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.metrics import confusion_matrix


cd_data = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/dogs_n_cats.csv')
X = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/dogs_n_cats.csv').drop(['Вид', 'Высота', 'Шерстист'], axis=1)
test = pd.read_json('C:/Users/ediga/Projects/Python_Ln/Data/Files/dataset_209691_15 (1).txt').drop(['Высота', 'Шерстист'], axis=1)
y = cd_data.Вид

dt = DecisionTreeClassifier()
parametrs = {'criterion': ['gini', 'entropy'], 'max_depth': range(1, 10), 'min_samples_split': range(2, 10), 'min_samples_leaf': range(1, 10)}

# search = GridSearchCV(dt, parametrs, cv=5)
# search.fit(X, y)
# перебор всех возможных деревьев

search = RandomizedSearchCV(dt, parametrs, cv=5)
search.fit(X, y)
# выбор лучшего дерева, чуть быстрее

best_tree = search.best_estimator_
predictions = best_tree.predict(test)
conf_matrix = confusion_matrix(y, predictions)
