import sys 
for data in sys.stdin:
    data = data.strip().split() 
    for word in data: 
        print ('%s%s%d' % (word, '\t', 1)) 


