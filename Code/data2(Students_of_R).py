import pandas as pd
import numpy as np

events_data = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/event_data_train.zip', compression='zip')
events_data['date'] = pd.to_datetime(events_data.timestamp, unit='s')  # перевели дату в более удобный формат
events_data['day'] = events_data.date.dt.date
sub_data = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/submissions_data_train.csv')
sub_data['date'] = pd.to_datetime(sub_data.timestamp, unit='s')
sub_data['day'] = sub_data.date.dt.date
users_scores = sub_data.pivot_table(index='user_id',
                                    columns='submission_status',
                                    values='step_id',
                                    aggfunc='count',
                                    fill_value=0).reset_index()
users_events_data = events_data.pivot_table(index='user_id',
                                            columns='action',
                                            values='step_id',
                                            aggfunc='count',
                                            fill_value=0).reset_index()
gap_data = events_data[['user_id', 'day', 'timestamp']].drop_duplicates(subset=['user_id', 'day']) \
      .groupby('user_id')['timestamp'].apply(list).apply(np.diff).values
gap_data = pd.Series(np.concatenate(gap_data, axis=0))
gap_data = gap_data / (24 * 60 * 60)  # интересный перевод в дни
# print(gap_data[gap_data < 290].hist())  # собственно сам график
# print(gap_data.quantile(0.90))
# print(1)
# events_data.sort_values(['correct'], ascending=False).groupby('user_id').head(5)  # вычисляем Анатолия))
events_data.groupby('user_id')['day'].nunique().idxmax()  # Пользователь, который провел на курсе больше всего дней
users_data = events_data.groupby('user_id', as_index=False) \
    .agg({'timestamp': 'max'}).rename(columns={'timestamp': 'last_timestamp'})
now = 1526772811
drop_out_treshold = 259200  # тридцать дней (30 * 24 * 60 * 60)
users_data['is_gone_user'] = (now - users_data.last_timestamp) > drop_out_treshold
# финальный тайимстемп с *хвоста датафрейма минус последний таймстеп юзера
users_data = users_data.merge(users_scores, on='user_id', how='outer').fillna(0)
# объединяем таблицы, атрибут how говорит, что не хотим терять строки пустые, заполняем их nan
users_data = users_data.merge(users_events_data, how='outer')
users_days = events_data.groupby('user_id').day.nunique().to_frame().reset_index()
# coздаем пандовскую серию, сколько дней у юзера, после переводим в датафрейм
users_data = users_data.merge(users_days, how='outer')
users_data['passed_course'] = users_data.passed > 170
# print(users_data.groupby('passed_course').count())
users_data[users_data.passed_course].day.median()
users_min_time = events_data.groupby('users_id', as_index=False).agg({'timestamp': 'min'}) \
    .rename({'timestamp': 'min_timestamp'}, axis=1)
users_data = users_data.merge(users_min_time, how='outer')
events_data
