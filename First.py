import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from collections import Counter

data = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/invasion.csv')
X = data.drop(['class'], axis=1)
X = pd.get_dummies(X)
X = X.fillna('null')
y = data.rename(columns={
    'class': 'target'
})
y = y.target
y = pd.get_dummies(y)

X_test = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/operative_information.csv')

clf_rf = RandomForestClassifier()
parametrs = {
    'n_estimators': list(range(10, 50, 10)),
    'max_depth': list(range(1, 12, 2)),
    'min_samples_leaf': list(range(1, 7)),
    'min_samples_split': list(range(2, 9, 2))
}
grid_search_cv_clf = GridSearchCV(clf_rf, parametrs, cv=3, n_jobs=-1)

grid_search_cv_clf.fit(X, y)
best_clf = grid_search_cv_clf.best_estimator_
predicitions = grid_search_cv_clf.predict(X_test)
y = pd.DataFrame(predicitions)
print(np.count_nonzero(predicitions, axis=1))
