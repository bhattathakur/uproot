1. import pandas as pd
1. df=pd.read_csv('',sep='\t') 
1. type(df)
1. df.shape()
1. df.columns
1. df.rows
1. df.info
1. df.head()
1. df.tail()
1. new_column=df['name']
1. column_list=df[[members of list]]
1. loc->Subset based on index label (row name)
1. iloc->Subset based on index label or row index
1. number of rows->df.shape[0]
1. last index->df[number of rows-1]#data frame
1. df.tail(n=1)#data frame
1. df.loc[0]#series Series
1. df.head(n=1) #data frame
1. df.iloc[-1] # iloc allows to use -1 (negative index)
