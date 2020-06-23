import pandas as pd
import numpy as np
import seaborn as sns

events_data = pd.read_csv('C:/Users/ediga/Downloads/event_data_train.csv')
events_data['date'] = pd.to_datetime(events_data.timestamp, unit='s')  # перевели дату в более удобный формат
events_data['day'] = events_data.date.dt.date
sub_data = pd.read_csv('C:/Users/ediga/Downloads/submissions_data_train.csv')
sub_data['date'] = pd.to_datetime(sub_data.timestamp, unit='s')
sub_data['day'] = sub_data.date.dt.date
users_scores = sub_data.pivot_table(index='user_id',
                                    columns='submission_status',
                                    values='step_id',
                                    aggfunc='count',
                                    fill_value=0).reset_index()
gap_data = events_data[['user_id', 'day', 'timestamp']].drop_duplicates(subset=['user_id', 'day']) \
      .groupby('user_id')['timestamp'].apply(list).apply(np.diff).values
gap_data = pd.Series(np.concatenate(gap_data, axis=0))
gap_data = gap_data / (24 * 60 * 60)  # интересный перевод в дни
print(gap_data[gap_data < 290].hist())  # собственно сам график
print(gap_data.quantile(0.90))

