import pandas as pd
import numpy as np
dates=pd.date_range('20130101', periods=100)
df = pd.DataFrame(np.random.randn(100,4), index=dates, columns=list('ABCD'))
# To view last 5 records
print(df.tail())
# To view the index
print(df.index)
# To view the column names
print(df.columns)
# Sorting by Axis
print(df.sort_index(axis=1, ascending=False).head())
# Sorting by Values
print(df.sort_values(by='B').head(3))
# Slicing the rows
print(df[0:3])
# Slicing with index name
print(df['20130105':'20130110'])
# Slicing with row and column index (like 2D Matrix)
print(df.iloc[0])
# will fetch 1 st row, first 2 columns
print(df.iloc[0,:2])
# will fetch 1 st row, 1 st column element
print(df.iloc[0,0])
# Selecting a single column
print(df['A'].head())
# Selecting more than one column
print(df[['A','B']][:5])
# Selecting more than one column, with selected number of records
print(df.loc['20130101':'20130105'][:2])

# Boolean Indexing
print("bool")
print(df[df.A>1])
# Setting by assigning with a numpy array
df.loc[:,'D']=np.array([5]*len(df))

# Deleting a row or column
df.drop('C',axis=1,inplace=True)
df.drop('20130101',axis=0,inplace=True)