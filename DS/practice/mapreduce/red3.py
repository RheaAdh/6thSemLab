import fileinput

for line in fileinput.input():
    line=line.strip().split(',')
    
    date,time,state,category,amt,mode=line
    if float(amt)>float(300.0):
        print("amt:{1},date:{0}".format(date,amt))
