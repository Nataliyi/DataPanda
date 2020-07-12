import pandas as pd


sf = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/StudentsPerformance.csv')

print(sf.loc[sf.gender == 'female', ['gender', 'writing score']])  # фильтрация по составу с выборкой некоторых столбцов
mean = sf['writing score'].mean()  # а найдем ка среднее значение столбца
print(sf.loc[sf['writing score'] > mean])  # все значения, больше среднего
cut = (sf.loc[sf.lunch == 'free/reduced', ['math score', 'reading score', 'writing score']])
print(sf.describe() - cut.describe())
sf = sf.rename(columns={
    'writing score': 'writing_score'
})  # переименовываем колонки
print(sf.head())
print(sf.query('writing_score > 75'))  # вот такая необычная фильтрация в pandas))
print(sf.query(
    "gender == 'female'"))  # вот такая необычная фильтрация в pandas, здесь мы используем разные кавычки для строки))
wsq = 78
print(sf.query(
    "writing_score > @wsq"))  # вот такая необычная фильтрация в pandas, здесь мы экранируем переменную c помощью @
print(sf.filter(like='score'))  # шикарный фильтр по колонкам, часть строки
# и еще один пример, если б наши id были именами:
# sf_name.filter(like='e', axis=0), где axis означает, что хотим фильтровать по строкам, а не столбцам
selected_columns = sf.filter(like='score')
