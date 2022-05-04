from itertools import groupby 
from operator import itemgetter 
import sys 

def main(separator='\t'): 
    for line in sys.stdin:
        data = line.rstrip().split(separator, 1)  
        # print(data)
        for current_word, group in groupby(data, itemgetter(0)): 
            print(current_word,group)
            try: 
                total_count = sum(int(count) for current_word, count in group) 
                print(total_count)
                print ("%s%s%d" % (current_word, separator, total_count)) 
            except ValueError:
                pass 

if __name__ == "__main__": 
    main() 