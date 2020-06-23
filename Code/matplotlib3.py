import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('C:/Users/ediga/Downloads/genome_matrix.csv', index_col=0)
dt = pd.read_csv('C:/Users/ediga/Downloads/dota_hero_stats.csv')

g = sns.heatmap(data=data, cmap='viridis')
# ваш код для создания теплокарты, укажите параметр cmap=viridis для той же цветовой схемы
g.xaxis.set_ticks_position('top')
g.xaxis.set_tick_params(rotation=90)

lenth = [len(r.split(',')) for r in dt.roles]
# преобразовываем списки в строках в длину и столбец
dt['lenths'] = lenth
print(dt['lenths'].mode())
# мода!! Опять забыла! Наибльшее встречающееся


plt.show()






