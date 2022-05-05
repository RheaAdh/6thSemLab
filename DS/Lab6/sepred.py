from itertools import groupby 
from operator import itemgetter 
import sys 


for line in sys.stdin:
    data = line.rstrip().split('\t', 1)  
    # print(data)

        try: 
            total_count = sum(int(count) for current_word, count in group) 
            print(total_count)
            print ("%s%s%d" % (current_word, '\t', total_count)) 
        except ValueError:
            pass 

