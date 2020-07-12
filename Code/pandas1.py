import pandas as pd
import numpy as np

spf = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/StudentsPerformance.csv')
print(spf.describe())  # статистикааа!!!)))))Боги Питона, благодарю!
print(spf.iloc[0:6, 0:3])  # вывод по индексу index location
print(spf.iloc[[0, 3, 10], [0, 4, 6]])  # вывод по строкам index location
spf_with_name = spf.iloc[[0, 3, 4, 7, 8]]
spf_with_name.index = ['Cersey', 'Yaris', 'Gregor', 'Andy', 'Peter']
print(spf_with_name.loc[['Cersey', 'Andy'], ['reading score', 'gender']])  # вывод строк по названию строк и столбцов
print(spf_with_name.iloc[:, 1])  # пандас серия

# создадим свой датафрейм:
my_series_1 = pd.Series([1, 2, 3], index=['Ilia', 'Carry', 'Panda'])
my_series_2 = pd.Series([0, 5, 8], index=['Clara', 'Cry', 'Daddy'])
my_df = pd.DataFrame({'col_name_1': my_series_1, 'col_name_2': my_series_2})
print(my_df)
print(spf.loc[:7])
print(spf.iloc[:7])

tds = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/titanic.csv')
print(tds.info())  # полная информация о датафрейме
