import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/iris.csv')
data = data.drop(columns='species')
data = data.drop(columns='Unnamed: 0')

# for column in data:
#     sns.distplot(data[column])  # строим график!)))
#     sns.kdeplot(data[column])  # подписывает значения, удобно

# sns.violinplot(y=data['petal length'])  # длина лепестков, красота!))
sns.pairplot(data=data)

plt.show()