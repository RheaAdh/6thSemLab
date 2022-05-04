import pandas as pd
import numpy as np
data1=[[1,2],[3,4],[5,6]]
data2=[[1,2],[3,4],[5,6]]
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
df_new1=pd.concat([df1,df2],axis=1)
print(df_new1.shape)
df_new2=pd.concat([df1,df2],axis=0)
print(df_new2.shape)