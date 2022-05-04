import fileinput
cnt=0
for line in fileinput.input():
    line=line.strip().split('\t')
    x,y=line
    cnt+=y
    print("{},{}",x,y)
print("number of even numbers:",cnt)