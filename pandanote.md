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
1. df.loc[0]#series 
1. df.head(n=1) #data frame
1. df.iloc[-1] # iloc allows to use -1 (negative index)
1. range(start=0,stop,step=1)                             
1. slicing syntax can be used in row for both loc and iloc
1. df.groupby(['parameters from row'])[[selection from columns]].applicaiton funciton
1. groupbyvarname.reset_index()
1. nunique()->Gives unique number of elements
1. plt.style.use('dark_background') # helps to show the axis labels in dark mode
1. Data Series can be created with pd.Series([values list],index=[ row names])
