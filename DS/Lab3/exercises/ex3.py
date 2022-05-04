import numpy as np
# Create ndArray from a list
npArray = np.array([1,2,3,4,5,6,7,8,9])
print('Contents of the ndArray : ')
print(npArray)
# Create ndArray from a tuple
npArray = np.array( (11,22,33,44,55,66,77,88 ) )
print('Contents of the ndArray : ')
print(npArray)
#create 3x4 array with 0
z=np.zeros((3,4))
print(z)
# sequence from 0 to 20 with steps of 5
print(list(range(0,21,5)))
# reshape matrix
a = np.array([[1,2,3,10], [4,5,6,9], [1,2,3,4]])
print("a=")
print(a)
print(a.shape) 
print("b=")
b = np.reshape(a, (2,2,3)) 
print(b)
print(b.shape)
# min max sum of matrix
mat=np.array([[1,2,3],[4,5,6],[7,8,9]])
# 1 2 3
# 4 5 6
# 7 8 9
i=0
for x in mat:
    print(i," row =")
    print("sum=",np.sum(x))
    print("min=",x.min())
    print("max=",x.max())
    i+=1


colsumarr=np.sum(mat,axis=0)
colmaxarr=np.max(mat,axis=0)
colminarr=np.min(mat,axis=0)
i=0
for x in range(0,len(colsumarr)):
    print("col idx =",i)
    print("sum=",colsumarr[x])
    print("min=",colminarr[x])
    print("max=",colmaxarr[x])
    i+=1