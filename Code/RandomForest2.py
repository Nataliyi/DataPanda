from Tools.scripts.dutree import display
from sklearn import tree
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import zipfile
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV


data = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/training_mush.csv')
X = data.drop(['class'], axis=1)
X = pd.get_dummies(X)
X = X.fillna('null')
y = data.rename(columns={
    'class': 'target'
})
y = y.target

data_test = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/testing_mush.csv')

clf_rf = RandomForestClassifier(random_state=0)
parametrs = {
    'n_estimators': list(range(10, 50, 10)),
    'max_depth': list(range(1, 12, 2)),
    'min_samples_leaf': list(range(1, 7)),
    'min_samples_split': list(range(2, 9, 2))
}
grid_search_cv_clf = GridSearchCV(clf_rf, parametrs, cv=3, n_jobs=-1)
# n_jobs - параметр для ускорения, чтобы использовать все процессоры
# cv - количество выборок

grid_search_cv_clf.fit(X, y)
best_clf = grid_search_cv_clf.best_estimator_
feature_importances = best_clf.feature_importances_
feature_importances_df = pd.DataFrame({
    'features': list(X),
    'feature_importances': feature_importances
})
# print(feature_importances_df.sort_values('feature_importances', ascending=False))
predicitions = grid_search_cv_clf.predict(data_test)

z = zipfile.ZipFile("C:/Users/ediga/Projects/Python_Ln/Data/Files/testing_y_mush.csv.zip", 'r')
txtfile = z.extract('testing_y_mush.csv', pwd='Cool!Move_forward!'.encode('cp850', 'replace'))
y_true = pd.read_csv(txtfile)
# opening protected csv

confusion_matrix(y_true, predicitions)

sns.heatmap(confusion_matrix(y_true, predicitions), annot=True, annot_kws={"size": 16}, cmap='Blues')