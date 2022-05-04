tup = (12, 7, 38, 56, 78)
eventup = ()
for x in tup:
    if(x % 2 == 0):
        eventup = eventup + (x,)
print(eventup)
