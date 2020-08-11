import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.metrics import roc_curve, auc


# dt = tree.DecisionTreeClassifier(max_depth=5, min_samples_split=5)

tree_data = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/train_data_tree.csv')
X = tree_data.drop(['num'], axis=1)
y = tree_data.num
clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=2)
clf.fit(X, y)
tree.plot_tree(clf.fit(X, y), feature_names=list(X), filled=True)
res = 0.996 - (157*0.903 + 81*0.826) / 238
# IG = 0.996 - (n0*E0 + n1*E1)/N
# n0 - чило сэмплов слева, n1 - число сэмплов справа,
# E0 - энтропия слева, Е1 - энтропия справа. N = n0+n1
IG = clf.tree_.impurity[0] - (clf.tree_.n_node_samples[1] * clf.tree_.impurity[1] +
              clf.tree_.n_node_samples[4] * clf.tree_.impurity[4]) / clf.tree_.n_node_samples[0]
