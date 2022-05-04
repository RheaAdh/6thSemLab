import pandas as pd
import matplotlib.pyplot as plt 
df = pd.read_csv('diabetes.csv',header=None)
print(df.head())
df.columns=['preg','glu','bp','sft','ins','bmi','dpf','age','class']
# print(plt.scatter(df['bmi'],df['glu']))
plt.xlabel('bmi')
plt.ylabel('Glucose')
df['age'].hist()
plt.show()


