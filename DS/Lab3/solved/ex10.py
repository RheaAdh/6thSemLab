import numpy as np
b=np.arange(12).reshape(3,4)
print(b)
print("sum of each col")
print(b.sum(axis=0))
print("sum of each row")
print(b.sum(axis=1))