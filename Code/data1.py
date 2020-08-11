import pandas as pd
import seaborn as sns

sns.set(rc={'figure.figsize': [9, 6]})  # заранее меняем размер ячеек в плот для красивого отображения
events_data = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/event_data_train.csv')
print(events_data.head(10))
print(events_data.action.unique())  # смотрим, что за данные есть в колонке
events_data['date'] = pd.to_datetime(events_data.timestamp, unit='s')  # перевели дату в более удобный формат
print(events_data.dtypes)
print(events_data.date.min())
events_data['day'] = events_data.date.dt.date
print(events_data.groupby('day').user_id.nunique().head())
print(events_data.groupby('day').user_id.nunique().plot())  # рисуем красивый график))
print(events_data[events_data.action == 'passed'].groupby('user_id', as_index=False).agg({'step_id': 'count'}).rename(columns={'step_id': 'passed_steps'}).hist())
print(events_data.pivot_table(index='user_id', columns='action', values='step_id', aggfunc='count', fill_value=0).reset_index().head())  # создаем новую таблицу, удобно. Устанавливаем индексы
print(events_data.pivot_table(index='user_id', columns='action', values='step_id', aggfunc='count', fill_value=0).reset_index().discovered.hist())  # Смотрим новый полный и правильный график
