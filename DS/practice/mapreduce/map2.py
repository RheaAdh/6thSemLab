# gender wise show chol level in desc order
# how many men and women 
i=0

import fileinput

for line in fileinput.input():
    line=line.strip().split(',')
    if(i!=0 and len(line)==14):
        age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,target=line
        print("{}\t{}\t{}".format(sex,chol,age))
    i=i+1


