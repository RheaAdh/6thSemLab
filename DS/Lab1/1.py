Rhea Adhikari
CSE D
190905156

prog1.py -
counter = 100
miles = 1000.0
name = "Rhea"
print(counter)
print(miles)
print(name)

output -
student@dslab-12:~/Documents/190905156 $ python prog1.py
100
1000.0
Rhea

prog2.py
a = b = c = 1
print(a,b,c)
a,b,c = 1,2,"Rhea"
print(a,b,c)

output -
student@dslab-12:~/Documents/190905156 $ python prog2.py
1 1 1
1 2 Rhea

prog3.py
a = 5
b = 4.56
print(5*a)
print(a/2)
print(a**2)

output -
student@dslab-12:~/Documents/190905156 $ python prog3.py
25
2.5
25

prog4.py
str = 'Hello World'
print(str)
print(str[0])
print(str[2:5])
print(str[2:])
print(str * 2)
print(str + "TEST")
output -
student@dslab-12:~/Documents/190905156 $ python prog4.py
Hello World
H
llo
llo World
Hello WorldHello World
Hello WorldTEST

prog5.py 
var1 = 'Hello World'
print("Updated String:",var1[:6]+'Python')
print("My name is %s and weight is %d kg!"%('Anitha',55))
str = "this is string example....wow!!!"
print(str.capitalize())
str = "this is string example....wow!!!"
print(str.count('s'))
str = "this is string example....wow!!!"
print(str.find('example'))
str = "THIS IS STRING EXAMPLE....WOW!!!"
print(str.lower())
str = "this is string example....wow!!!"
print(str.replace("is","was"))
str = "this is string example....wow!!!"
print(str.swapcase())
str = "this is string example....wow!!!"
print(str.title())

output -
student@dslab-12:~/Documents/190905156 $ python prog5.py
Updated String: Hello Python
My name is Anitha and weight is 55 kg!
This is string example....wow!!!
3
15
this is string example....wow!!!
thwas was string example....wow!!!
THIS IS STRING EXAMPLE....WOW!!!
This Is String Example....Wow!!!

prog6.py
list = ['abcd',786,2.23,'Rhea',70.2]
tinylist = [233,'Rhea']
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist*2)
print(list+tinylist)

output -
student@dslab-12:~/Documents/190905156 $ python prog6.py
['abcd', 786, 2.23, 'Rhea', 70.2]
abcd
[786, 2.23]
[2.23, 'Rhea', 70.2]
[233, 'Rhea', 233, 'Rhea']
['abcd', 786, 2.23, 'Rhea', 70.2, 233, 'Rhea']

prog7.py
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

output -
student@dslab-12:~/Documents/190905156 $ python prog7.py
['physics', 'chemistry', 1997, 2000, 'maths']
['physics', 'chemistry', 2000, 'maths']
True
False
4
1
['physics', 'chemistry', 1997]
['physics', 'chemistry', 'maths', 1997, 2000]
['physics', 1997, 2000]
[2000, 1997, 'chemistry', 'physics']

prog8.py
tuple = ('abcd',786,2.23,'Rhea',70.2)
list = ['abcd',786,2.23,'Rhea',70.2]
tuple[2] = 1000
list[2] = 1000
print(tuple)
print(list)

output -
Traceback (most recent call last):
  File "prog8.py", line 3, in <module>
    tuple[2] = 1000
TypeError: 'tuple' object does not support item assignment

on commenting tuple[2] = 1000 output -
student@dslab-12:~/Documents/190905156 $ python prog8.py
('abcd', 786, 2.23, 'Rhea', 70.2)
['abcd', 786, 1000, 'Rhea', 70.2]

eg1.py
num = float(input('Enter a number:'))
if num>0:
	print('pos number')
elif num == 0:
	print('zero')
else:
	print('Neg number')

output -
student@dslab-12:~/Documents/190905156 $ python eg1.py
Enter a number:10
pos number

eg2.py
x = float(input('Enter a number:'))
if x<10:
	print('smaller')
if x>20:
	print('bigger')
print('Finished')

output -
student@dslab-12:~/Documents/190905156 $ python eg2.py
Enter a number:5
smaller
Finished

eg3.py
x = 5
print('Before 5')
if x == 5:
	print('this is 5')
	print('still 5')
print('After 5')
print('Before 6')
if x == 6:
	print('this is 6')
print('After 6')

output -
student@dslab-12:~/Documents/190905156 $ python eg3.py
Before 5
this is 5
still 5
After 5
Before 6
After 6

eg4.py (which will never print)
x = float(input('Enter a number:'))
if x<20:
	print('Below 20')
elif x<10:
	print('Below 10')
else:
	print('something else')

output -
student@dslab-12:~/Documents/190905156 $ python eg4.py
Enter a number:5
Below 20

print(‘Below 10’) will never be displayed

eg5.py
x = 42
if x>1:
	print('above one')
	if x<100:
		print('less than 100')
print('All done')

output -
student@dslab-12:~/Documents/190905156 $ python eg5.py
above one
less than 100
All done

eg6.py
age = 15
b = ('kid' if age<18 else 'adult')
print(b)

output -
student@dslab-12:~/Documents/190905156 $ python eg6.py
kid

EG1.py
for val in [5,4,3,2,1]:
	print(val)
print('Done')

output -
student@dslab-12:~/Documents/190905156 $ python EG1.py
5
4
3
2
1
Done

EG2.py
stud = ['Seema','Aashna','Juhi','Rhea','Ramesh','Suma']
for k in  stud:
	print('Hello:',k)
print('done')

output -
student@dslab-12:~/Documents/190905156 $ python EG2.py
Hello: Seema
Hello: Aashna
Hello: Juhi
Hello: Rhea
Hello: Ramesh
Hello: Suma
done

EG3.py
for i in range(5):
	print(i)
	if i > 2:
		print('Bigger than 2')
	print('Done with i',i)

output -
student@dslab-12:~/Documents/190905156 $ python EG3.py
0
Done with i 0
1
Done with i 1
2
Done with i 2
3
Bigger than 2
Done with i 3
4
Bigger than 2
Done with i 4

EG4.py
x = int(input('Enter a number:'))
for i in range(1,x+1):
	if x%i == 0:
		print(i)

output -
student@dslab-12:~/Documents/190905156 $ python EG4.py
Enter a number:10
1
2
5
10

EG5.py
from math import *
x = [9,41,23,3,74,15]
Largest = -inf
for i in x:
	if i > Largest:
		Largest = i
print(Largest)

output -
student@dslab-12:~/Documents/190905156 $ python EG5.py
74

EG6.py
from math import *
x = [9,41,23,3,74,15]
smallest = inf
for i in x:
	if i < smallest:
		smallest = i
print(smallest)

output -
student@dslab-12:~/Documents/190905156 $ python EG6.py
3

EG7.py
x = [9,41,23,3,74,15]

count = sum = avg = 0

for i in x:
	count = count+1
	sum = sum+1
avg = sum/count

print(count)
print(sum)
print(avg)

output -
student@dslab-12:~/Documents/190905156 $ python EG7.py
6
6
1.0

EG8.py
x = [9,41,23,3,74,15]

for i in x:
	if i>20:
		print(i)

output -
student@dslab-12:~/Documents/190905156 $ python EG8.py
41
74

EG9.py
x = [9,41,23,3,74,15]
res = []
for i in x:
	if i>20:
		res.append(i)
print(res)

output -
student@dslab-12:~/Documents/190905156 $ python EG9.py
[41, 74]

EG10.py
import numpy as np 
x = [9,41,23,3,74,15]
y = np.zeros(len(x))

for i in range(len(x)):
	if x[i]>20:
		y[i] = x[i]

print(y)

output -
student@dslab-12:~/Documents/190905156 $ python EG10.py
[ 0. 41.  0.  0. 74.  0.]