import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sf = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/StudentsPerformance.csv')
ic = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/income.csv')
sf = sf.rename(columns={
    'math score': 'math_score',
    'reading score': 'reading_score',
    'writing score': 'writing_score'
})
sfg = sf.math_score.hist()  # реализуем данные гистогррамы
# plt.show()  # выводим гистограмму на экран

sf.plot.scatter(x='math_score', y='reading_score')  # график q-plot... Да-да, он самый!)))

ax = sns.lmplot(data=sf, x='math_score', y='reading_score', hue='gender', fit_reg=False)
# оно же в другой библиотеке, удобнее
ax.set_xlabels('Math score')  # поменяли имя прямым
ax.set_ylabels('Reading score')
plt.show()



