from Tools.scripts.dutree import display
from sklearn import tree
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import GridSearchCV


data = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/33180_43520_bundle_archive.zip', compression='zip')
X = data.drop(['target'], axis=1)
y = data.target

np.random.seed(0)

rf = RandomForestClassifier(10, max_depth=5)
rf.fit(X, y)
imp = pd.DataFrame(rf.feature_importances_, index=X.columns, columns=['importance'])
imp.sort_values('importance').plot(kind='barh', figsize=(12, 8))
# просто обучили рандомное дерево и нарисовали график по важности фичей


