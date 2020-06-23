import pandas as pd
import numpy as np


my_stat = pd.read_csv('C:/Users/ediga/Downloads/my_stat (1).csv')
subset_1 = my_stat.iloc[0:10, [0, 2]]
subset_2 = my_stat.drop([0, 4], axis=0)  # удаление лишних строк
subset_2 = subset_2.iloc[:, [1, 3]]
subset_3 = my_stat.query('V3 == "A" and V1 > 0')
subset_4 = my_stat.query('V2 != 10.00000 or V4 >= 1')
my_stat['V5'] = my_stat.V1 + my_stat.V4
my_stat['V6'] = np.log(my_stat.V2)
my_stat = my_stat.rename(columns={
'V1': 'session_value',
'V2': 'group',
'V3': 'time',
'V4': 'n_users'
})
my_stat.session_value = my_stat.session_value.fillna(0)  # замена nan значений на 0
M = my_stat[my_stat.n_users >= 0.0].n_users.median()
my_stat.loc[my_stat['n_users'] < 0, 'n_users'] = M
mean_session_value_data = my_stat.groupby('group', as_index=False).agg({'session_value': 'mean'}).rename(columns={'session_value': 'mean_session_value'})