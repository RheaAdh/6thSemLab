# no.of deaths,recovered,confirmed country wise
import fileinput

prevstate=None
d=0
c=0
r=0

for line in fileinput.input():
    line=line.strip().split('\t')
    if(len(line)==4):
        state,confirmed,deaths,recovered=line
        confirmed=int(confirmed)
        deaths=int(deaths)
        recovered=int(recovered)
        if prevstate==None:
            prevstate=state
            d=deaths
            r=recovered
            c=confirmed
            continue
        if(prevstate==state):
            d=d+deaths
            r=r+recovered
            c=c+confirmed
        else:
            if(d>1000000):
                print("%s\t%d\t%d\t%d"%(prevstate,c,d,r))
            prevstate=state
            d=deaths
            r=recovered
            c=confirmed
    
print("%s\t%d\t%d\t%d"%(prevstate,c,d,r))