import pandas as pd

def getInsightsDef():
   """method to read the insights definitions into a pandas dataframe"""
   df = pd.read_csv('input/insights_def.tsv', delimiter='|', encoding='utf-8')

   print(df)
   # print(df.iloc[1])

   return df

# getInsightsDef()

