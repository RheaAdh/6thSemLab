# no.of deaths,recovered,confirmed country wise

import fileinput
p=0
for x in fileinput.input():
    if p is not 0:
        data=x.strip().split(',')
        # print(data)
        if(len(data)==8):
            id,date,state,country,last_updated,confirmed,deaths,recovered= data
            print("{}\t{}\t{}\t{}".format(state,confirmed,deaths,recovered))
    p=p+1