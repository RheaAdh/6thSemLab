num = int(input('Enter number whose factors have to be found '))
for x in range(1,num):
    if (num % x)==0: 
        print (x)