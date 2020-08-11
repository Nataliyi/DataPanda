import pandas as pd
from sklearn import tree


data = pd.DataFrame({'X_1': [1, 1, 1, 0, 0, 0, 0, 1], 'X_2': [0, 0, 0, 1, 0, 0, 0, 1], 'Y': [1, 1, 1, 1, 0, 0, 0, 0]})
clf = tree.DecisionTreeClassifier(criterion='entropy')
X = data[['X_1', 'X_2']]
y = data.Y
tree.plot_tree(clf.fit(X, y), feature_names=list(X), class_names=['Negative', 'Positive'], filled=True)
# выводим дерево на экран, красота, только не понятно ничего пока))))
