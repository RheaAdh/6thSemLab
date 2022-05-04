import numpy as np
ppl=[12,13,6,23,43]
cnt=0
b=("kid" if ppl[1]<=18 else "adult")
print(b)
for age in ppl :
    if(age>18):
        cnt=cnt+1
print("No.of ppl adult= ",cnt )


for i in range(2,6):
    flag=0
    for j in range(2,i):
        if(i%j==0):
            flag=1
    if(flag==1): 
        print("%d is not prime" % i)
    else : 
        print("%d is prime"% i)



x= [9, 41, 12, 3, 74, 15]
Largest=-99999
for i in x:
    if i>Largest:
        Largest=i
print(Largest)

y=np.zeros(len(x))
for i in range(len(x)):
    if x[i]>20:
        y[i]=x[i]
for i in y:
    print i