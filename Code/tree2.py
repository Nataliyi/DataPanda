import pandas as pd
import numpy as np
import seaborn as sns
from sklearn import tree
from sklearn.model_selection import train_test_split


titanic_data = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/train.csv')
print(titanic_data.isnull().sum())  # пропущенные значения
X = titanic_data.drop(['PassengerId', 'Survived', 'Name', 'Ticket', 'Cabin'], axis=1)
X = pd.get_dummies(X)  # классная штука, заменяет значения, где возможно на 1 и 0
y = titanic_data.Survived
X = X.fillna({'Age': X.Age.median()})  # заполняем пустые значения медианой
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
# пока непонятно, что делаем

clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=5)
clf.fit(X, y)
tree.plot_tree(clf.fit(X, y), feature_names=list(X), filled=True)
print(clf.score(X, y))  # точность наблюдений
