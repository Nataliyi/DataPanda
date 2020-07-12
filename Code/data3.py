import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib
from sklearn import tree
from sklearn.model_selection import train_test_split, cross_val_score

titanic_data = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/train.csv')
# print(titanic_data.isnull().sum())  # пропущенные значения
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

scores_data = pd.DataFrame()
max_depth_values = range(1, 100)

for max_depth in max_depth_values:
    clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=max_depth)
    clf.fit(X_train, y_train)
    score = clf.score(X_train, y_train)
    test = clf.score(X_test, y_test)
    temp_score_data = pd.DataFrame({'max_depth': [max_depth],
                                    'score': [score],
                                    'test': [test]})
    scores_data = scores_data.append(temp_score_data)
scores_data_long = pd.melt(scores_data,
                           id_vars=['max_depth'],
                           value_vars=['score', 'test'],
                           var_name='set_type', value_name='score')
# преобразовываем две колонки в одну со значениями
# print(sns.lineplot(data=scores_data_long, x='max_depth', y='score', hue='set_type'))
clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=4)
print(cross_val_score(clf, X_train, y_train, cv=5))
# валидацияяя!!!!))))
print(scores_data_long.query('set_type == "cross_val_score"').head(20))
print(cross_val_score(clf, X_test, y_test, cv=5).mean())