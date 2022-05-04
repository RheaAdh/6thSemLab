# Assigning Values to Variables
name = "John" 
a = b = c = 1

# Multiple Assignment
a, b, c = 10, 20, "Sam"
print (name)
print (a)
print (b/2)
print(c)

# Standard Data Types
## numbers
a = 5
b= 4.5
print (5*a)
print (a/2)
print (a//2)
print(a**2)

##string
str = 'Hello World!'
print (str) 
print (str[0]) 
print (str[2:5]) 
print (str[2:])
print (str * 2)
print (str + "TEST")
print ("Updated String :", str[:6] + 'Python')
name='rhea adhikari'
print( "My name is %s and weight is %d kg!" % (name, 55))
print( "My name is %s and weight is %d kg!" % (name.capitalize(), 55))
print( "My name has %d 'i' letters!" % (name.count('i')))
print(name.find("Adh"))
print(name.find("adh"))
print(name.title().swapcase())
print(name.replace('rhea','Rhea'))

# Lists
list = [ 'rhea', 123 , 23.23]
tinylist = [123, 'john']
print (list)
print (list[1:3]) 
print (list[2:])
list.append((list+tinylist*2)[0][3]*5)
print (list) 
print('rhea' in list)
del list[2]
list.append('rhea')
print('original',list.count('rhea'))
list.reverse()

# Tuple - Read Only

tuple = ( 'rhea', 71 , 3.23, 'ABC', 70.2 )
# tuple[2] = 1000 # Invalid syntax with tuple