import numpy as np
mat=np.array([[1,2,3],[4,5,6],[7,8,9]])
colsum=np.sum(mat, axis=0)   ### column-wise sums
rowsum=np.sum(mat, axis=1)   ### row-wise sums   
print(colsum)
print(rowsum)