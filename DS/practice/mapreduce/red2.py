# gender wise show chol level in desc order
# how many men and women 
import fileinput
men=0
women=0
for line in fileinput.input():
    line=line.strip().split('\t')
    if(len(line)==3):
        sex,chol,age=line
        sex=int(sex)
        chol=int(chol)
        age=int(age)
        print(line)
        if(chol>200):
            if(sex==0):
                women=women+1
            else:
                men=men+1
print("No.of women with cholestrol levels above 200= {}".format(women))
print("No.of men with cholestrol levels above 200= {}".format(men))
