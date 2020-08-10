import pandas as pd


sub_data = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/submissions_data_train.csv')
users_max_timestamp = sub_data.groupby(['user_id'], as_index=False).aggregate({'timestamp': 'max'}).rename(columns={
    'timestamp': 'max_timestamp'
})
sub_data = sub_data.merge(users_max_timestamp, on='user_id')
# sub_data_train = sub_data.filter(items=['timestamp' == 'max_timestamp'], axis=1)
users_max_step = sub_data.groupby(['user_id'], as_index=False).aggregate({'step_id': 'max'}).rename(columns={
    'step_id': 'max_step_id'
})
sub_data_train = sub_data.loc[sub_data['timestamp'] == sub_data['max_timestamp']]
sub_data_train = sub_data_train.loc[sub_data_train['submission_status'] == 'wrong']
print(sub_data_train.step_id.value_counts())
print(sub_data.step_id.value_counts())