import pandas as pd

df = pd.read_excel('965.xlsx')
df = df.iloc[:, 11:]
df = df.transpose()
df.columns = ['distance_965']
df = df[::-1]
df.index = pd.date_range("2017-01-01", "2019-12-01", freq="M")

list.