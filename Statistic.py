import pandas as pd
import numpy as np
import seaborn as sns

events_data = pd.read_csv('C:/Users/ediga/Downloads/event_data_train.csv')
sub_data = pd.read_csv('C:/Users/ediga/Downloads/submissions_data_train.csv')
events_data['date'] = pd.to_datetime(events_data.timestamp, unit='s')  # перевели дату в более удобный формат
events_data['day'] = events_data.date.dt.date
print(events_data[['date', 'user_id']].min())
karp = sub_data.pivot_table(index='user_id',
                                    columns='submission_status',
                                    values='step_id',
                                    aggfunc='count',
                                    fill_value=0).reset_index()
print(karp.sort(karp.correct))