import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib
from sklearn import tree
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import f1_score, precision_score, recall_score

songs_data = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/songs.csv')


