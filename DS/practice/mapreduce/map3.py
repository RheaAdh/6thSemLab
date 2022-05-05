import fileinput

for line in fileinput.input():
    line=line.strip().split('\t')
    if(len (line)==6):
        date,time,state,category,amt,mode=line
        print("{},{},{},{},{},{}".format(date,time,state,category,amt,mode))