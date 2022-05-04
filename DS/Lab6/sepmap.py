import sys 

def main(separator='\t'): 
    for data in sys.stdin:
        data = data.strip().split() 
        for words in data: 
            for word in words: 
                print ('%s%s%d' % (word, separator, 1)) 


if __name__ == "__main__": 
    main() 