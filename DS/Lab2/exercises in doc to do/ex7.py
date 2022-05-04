mytuple = (1, 3, 5, 7, 9, 2, 4, 6, 8, 10)
l = len(mytuple)
cnt = 0
for x in mytuple:
    if(cnt < l/2):
        print(x)
    else:
        print('')
        cnt = 0
    print(" ")
    cnt += 1
