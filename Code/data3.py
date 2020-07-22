import pandas as pd
import seaborn
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import roc_curve, auc, precision_score, recall_score

titanic_data = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/train.csv')
# print(titanic_data.isnull().sum())  # пропущенные значения
X = titanic_data.drop(['PassengerId', 'Survived', 'Name', 'Ticket', 'Cabin'], axis=1)
X = pd.get_dummies(X)  # классная штука, заменяет значения, где возможно на 1 и 0
y = titanic_data.Survived
X = X.fillna({'Age': X.Age.median()})  # заполняем пустые значения медианой
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
# разбиваем датафрейм и серию на несколько переменных для теста и тренинга

clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=5)
clf.fit(X, y)
# tree.plot_tree(clf.fit(X, y), feature_names=list(X), filled=True)
# print(clf.score(X, y))  # точность наблюдений

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
# print(cross_val_score(clf, X_train, y_train, cv=5))
# # валидацияяя!!!!))))
# print(scores_data_long.query('set_type == "cross_val_score"').head(20))
# print(cross_val_score(clf, X_test, y_test, cv=5).mean())

parametrs = {'criterion': ['gini', 'entropy'], 'max_depth': range(1, 30)}
clf_2 = tree.DecisionTreeClassifier()
grid_search_cv_clf = GridSearchCV(clf_2, parametrs, cv=5)
grid_search_cv_clf.fit(X_train, y_train)
print(grid_search_cv_clf.best_params_)
# без всяких переборов, все делается за нас))) Лучшая глубина для выборки с валидацией
best_clf_2 = grid_search_cv_clf.best_estimator_
# записали лучший классификатор
print(best_clf_2.score(X_test, y_test))
y_pred = best_clf_2.predict(X_test)
# записываем предсказанное значение
print(precision_score(y_test, y_pred), recall_score(y_test, y_pred))
y_predicted_prob = best_clf_2.predict_proba(X_test)
print(pd.Series(y_predicted_prob[:, 1]).hist())
# построили более наглядную гистограмму, все проще и понятнее
y_pred2 = np.where(y_predicted_prob[:, 1] > 0.8, 1, 0)
# преобразовываем в 1 и 0 по заданным параметрам
print(precision_score(y_test, y_pred2), recall_score(y_test, y_pred2))

lw = 5
fpr, tpr, thresholds = roc_curve(y_test, y_predicted_prob[:,1])
roc_auc= auc(fpr, tpr)
plt.figure()
plt.plot(fpr, tpr, color='darkorange',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()
# строим график и смотрим результаты
