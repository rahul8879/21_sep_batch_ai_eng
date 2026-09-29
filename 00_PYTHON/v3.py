import pandas as pd

df = pd.read_csv("data.csv")
# print(type(df))
#print(df.head(5)) # select top 5 * from table
# print(df.columns)
# print(df.shape)
# print(df.info())
# print(df.isnull().sum())
# select col1, col2 from table where col1 > 5
# print(type(df['rating']))
# print(df[['rating','sadasd']])
    
# cond = df['rating'] > 3
# cond_2 = df['subjective_feedback'].notnull()
# print(df[cond & cond_2][['rating','session_name']].head())

cond_batc = df['session_name']=='Building APIs with FastAPI'
cond_batc_2 = df['rating'] <3
print(cond_batc)
final_df = df[cond_batc | cond_batc_2]
print(final_df)
# https://pandas.pydata.org/docs/getting_started/index.html