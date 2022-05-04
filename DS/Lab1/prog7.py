list = ['physics','chemistry',1997,2000]
list.append('maths')
print(list)

del list[2]
print(list)

print('physics' in list)

print('english' in list)

print(len(list))

print(list.count('physics'))

list = ['physics','chemistry',1997,2000]
list.pop()
print(list)

list = ['physics','chemistry',1997,2000]
list.insert(2,'maths')
print(list)

list = ['physics','chemistry',1997,2000]
list.remove('chemistry')
print(list)

list = ['physics','chemistry',1997,2000]
list.reverse()
print(list)
