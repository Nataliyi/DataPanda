import pandas as pd
import numpy as np

sf = pd.read_csv('StudentsPerformance.csv')
sf = sf.rename(columns={
    'math score': 'math_score',
    'reading score': 'reading_score',
    'writing score': 'writing_score'
})
print(sf.head())

print(sf.groupby('gender').mean())  # среднее значение

print(sf.groupby('gender').aggregate({'math_score': 'mean'}))  # по столбцу

print(sf.groupby('gender', as_index=False).aggregate({'math_score': 'mean'}))  # по столбцу, c индексом

mean_score = sf.groupby(['gender', 'race/ethnicity']).aggregate({'math_score': 'mean', 'reading_score': 'mean'}).rename(
    columns={'math_score': 'mean_math_score', 'reading_score': 'mean_reading_score'})
# новый датафрейм со средними значениями и мультииндексом.
# если в функции groupby() указать as_index=False, тогда датафрейм останется по индексу. Как работать с первым:
print(mean_score.loc[('female', 'group A')])

print(mean_score.loc[[('female', 'group A'), ('male', 'group A')]])  # если хочется еще колонок, то так

print(sf.math_score.unique())  # все уникальные числа в столбце

print(sf.math_score.nunique())  # сумма всех уникальных чисел в столбце

print(sf.sort_values(['gender', 'math_score'], ascending=False).groupby('gender').head(5))
#  сгруппировали по полу, топ 5 по математике отсортировали

sf['total_score'] = sf.math_score + sf.reading_score + sf.writing_score
# создали новую колонку с общими оценками

sf = sf.assign(total_score_log=np.log(sf['total_score']))
# создали новую колонку со значениями логарифмов для каждой ячейки

sf = sf.drop(['total_score'], axis=1)
# удалили колонку(axis - выбираем колонку, а не строку)



