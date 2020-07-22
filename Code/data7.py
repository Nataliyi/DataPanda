import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn import tree


iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
dt = tree.DecisionTreeClassifier()
dt.fit(X_train, y_train)
predicted = dt.predict(X_test)  # предсказание!

# cross_val_predict(estimator, x, y, cv=bar)
# Мы будем использовать другой способ - GridSearchCV, отбирающий
# лучшую модель по заданным параметрам, проводя кросс-валидацию.
