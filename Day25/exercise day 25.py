import pandas as pd

df = pd.read_csv('/storage/emulated/0/30 days of python/hacker_news.csv')

print ('first_5_rows:\n ',df.head())

print ('last_5_rows: ',df.tail())

print ('title_series: ',df.iloc[:,2])


python_title = df.loc[df['title'].str.contains('Python', case=False)]
print (python_title)

js_title = df.loc[df['title'].str.contains('JavaScript', case=False)]
print (js_title)
