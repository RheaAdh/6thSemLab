import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
W = pd.read_csv('wine_for_Week2.xls', header=None)
print(W.head())

D= np.loadtxt('xyz.txt',delimiter=",")
print(D[:5,:])

G=pd.read_excel('German Credit_for_Week2.xlsx',sheet_name='Sheet1',engine='openpyxl')
print(G.head())

H = pd.read_table('HR_for_Week2.txt')
H.head()

f=H['Department'].value_counts()
print(f)

f.plot(kind='bar')
plt.show()

f.plot(kind='pie')
plt.show()

fa=pd.crosstab(H['Gender'],H['Attrition'])
fa.plot(kind='bar')

plt.show()