import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib
from sklearn import tree
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import f1_score, precision_score, recall_score

precision = 15 / (15 + 15)  # tp / (tp + fp)
recall = 15 / (15 + 30)  # tp / (tp + fn)
f1 = 2 * (precision * recall) / (precision + recall)
# precision более важен в ситуациях, где не нужны ложные положительные срабатывания
# recall - там, где не нужны ложные отрицательные.
# precision = "не прихватить лишнее?"
#
# recall = "не пропустить нужное ?"
