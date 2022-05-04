li = [11, -21, 0, 45, 66, -93]
i = 0
while(i < len(li)):
    print(li[i])
    if(li[i] == 0):
        print("zero")
    elif(li[i] < 0):
        print("negative")
    else:
        print("positive")
    i += 1
