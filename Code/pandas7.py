import pandas as pd
import seaborn as sns


dt = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/space_can_be_a_dangerous_place.csv')

sns.heatmap(dt.corr(), annot=True)
# correlation!! nice view on heatmap
