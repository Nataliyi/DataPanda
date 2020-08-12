from Tools.scripts.dutree import display
from sklearn import tree
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV


titanic_data = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/train.csv')
# print(titanic_data.isnull().sum())  # пропущенные значения
X = titanic_data.drop(['PassengerId', 'Survived', 'Name', 'Ticket', 'Cabin'], axis=1)
X = pd.get_dummies(X)  # классная штука, заменяет значения, где возможно на 1 и 0
y = titanic_data.Survived
X = X.fillna({'Age': X.Age.median()})  # заполняем пустые значения медианой
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
# разбиваем датафрейм и серию на несколько переменных для теста и тренинга

clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3, min_samples_split=100, min_samples_leaf=10)

# max_depth - Максимальное число уровней дерева (максимальная длина пути от корня до листа)

# min_sample split - минимальный размер value для разбиения или
# Минимальное число образцов в узле, чтобы его можно было разделить на 2

# min_sample_leaf - минимальное количество sample для разбиения или
# Минимальное число образцов в листьях (при получившемся значении ниже разделение не будет произведено)

# min_impurity_decrease - Минимальное снижение "нечистоты"
# (смешения классов) узла при разделении, чтобы разделение произошло

clf.fit(X_train, y_train)

# tree.plot_tree(clf.fit(X_train, y_train), feature_names=list(X), filled=True)

# graph = Source(tree.export_graphviz(clf, out_file=None,
#                                     feature_names=list(X),
#                                     class_names=['Died', 'Survived'],
#                 stClassifier()                    filled=True))
# display(SVG(graph.pipe(format='svg')))


# random forest:
clf_rf = RandomForestClassifier()
parametrs = {'n_estimators': [10, 20, 30], 'max_depth': [2, 5, 7, 10]}
# n_estimators - количество деревьев
grid_search_cv_clf = GridSearchCV(clf_rf, parametrs, cv=5)
grid_search_cv_clf.fit(X_train, y_train)
print(grid_search_cv_clf.best_params_, grid_search_cv_clf.best_score_)

best_clf = grid_search_cv_clf.best_estimator_
feature_importances = best_clf.feature_importances_
feature_importances_df = pd.DataFrame({
    'features': list(X_train),
    'feature_importances': feature_importances
})
print(feature_importances_df.sort_values('feature_importances', ascending=False))
# параметр ascending - если хотим отсортировать по возрастанию, то True
