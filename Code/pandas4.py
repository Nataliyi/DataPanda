import pandas as pd

dt = pd.read_csv('C:/Users/ediga/Downloads/dota_hero_stats.csv')
ac = pd.read_csv('C:/Users/ediga/Downloads/accountancy.csv')
concentrations = pd.read_csv('C:/Users/ediga/Downloads/algae.csv')

print(dt.legs.value_counts())
# подсчет всех значений в столбце

print(ac.groupby(['Executor', 'Type']).aggregate({'Salary': 'mean'}))
print(ac.groupby(['Executor', 'Type']).aggregate({'Salary': 'max'}))
print(ac.groupby(['Type', 'Executor']).mean().unstack())  # возможно так удобнее
print(ac.groupby(['Type', 'Executor']).mean())  # или так :))
print(ac[ac['Executor'] == 'Pupa'].groupby(['Type']).agg({'Salary': 'mean'}))  # так себе...
print(ac.pivot_table(['Salary'], ['Type'], ['Executor'], aggfunc='mean'))  # неплохо)

print(dt.groupby(['attack_type', 'primary_attr']).aggregate({'primary_attr': 'count'}))
print(dt.filter(items=['attack_type', 'primary_attr']).mode())  # шикарное применение моды!))

mean_concentrations = concentrations.groupby('genus').mean()
#  среднее значение по каждой группе

con = concentrations.loc[concentrations.genus == 'Fucus', ['genus', 'alanin']]
print(con.describe())
print(concentrations.groupby('genus').aggregate({'alanin': ['min', 'mean', 'max']}).loc['Fucus'].round(2))
# прекрасная оптимальная замена. только не поняла. что значит round

print(concentrations.groupby('group').agg({
    'citrate': 'var',
    'sucrose': lambda x: x.max() - x.min(),
    'glucose': 'count'
})
      .round(2))
