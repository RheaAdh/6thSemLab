X = [[12,72],
    [4 ,15],
    [33 ,28]]
Y = [[12,72],
    [4 ,15],
    [33 ,28]]
Z = [[0,0],
    [0,0],
    [0,0]]
for i in range(0,len(X)):
    for j in range(0,len(X[0])):
        Z[i][j]=X[i][j]+Y[i][j]
for i in range(0,len(X)):
    for j in range(0,len(X[0])):
        print(Z[i][j],end=",")
    print('\n')
        