import pandas as pd

dt = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/movie_metadata.csv')
mt = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/movie_metadata.csv')

print(dt.duration.isna().sum())
# count of 'nun' values in column

test_dt = pd.DataFrame()
dt['duration'] = dt.duration.fillna(dt.duration.median())
# change 'nan' to median


dt['movie_duration_category'] = 'nan'
dt['duration1'] = dt.duration.astype(int)
# change 'float' values to 'int'

dt.loc[dt['duration1'] < 90, 'movie_duration_category'] = 'one'
dt.loc[(dt['duration1'] >= 90) & (dt['duration1'] <= 120), 'movie_duration_category'] = 'two'
dt.loc[dt['duration1'] > 120, 'movie_duration_category'] = 'three'
print(dt.movie_duration_category.unique())

dt['title_year1'] = dt['title_year'].fillna('0')
dt['title_year1'] = dt['title_year1'].astype(int)

dt['index'] = dt.index
pv = dt.pivot_table(columns='movie_duration_category',
                    index='index',
                    values='title_year1',
                    fill_value=0).reset_index()

www = pv.loc[pv['two'] == 2008]
print(www.two.count())
dt['movie_plot_category'] = dt['plot_keywords'].str.extract(r'\b(love)\b')

love = dt.pivot_table(columns='movie_plot_category',
                      index='index',
                      values='imdb_score',
                      fill_value=0).reset_index()


mt['budget'] = mt['budget'].map(lambda x: str(x)[:-1])

print(mt.budget.median())