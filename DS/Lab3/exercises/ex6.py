import numpy as np
X = [[1,2],
    [4 ,5],
    [3 ,2]]
Y = [[1,2,3,4],
    [1,6,5,2]]
m=len(X)
n=len(X[0])
p=len(Y)
q=len(Y[0])
if n!=p:
    print("Cannot multiply the matrices")
else:
    Z=np.zeros((m,q))
    # m*n X p*q = m*q where n=p
    
    # all n * all p and put in 
    for a in range(0,m):
        for b in range (0,q):
            sum=0
            for i in range(0,n):
                sum+=X[a][i]*Y[i][b]
                i+=1
            print(sum,end=",")
        print('\n')
