number = 23
running = 23
while running:
    guess = int(input('Enter an interger :'))
    if guess == number:
        print('Congratulation, you guessed it.') #New block starts here
        print('(but you do not win any prizes!)') #New block ends here
        running = False
    elif guess > number :
        print('No, it is a litter Lower than that') #Another block
    else:
        print('No, it is a litter Higher than that') #You must have guessed >number to reach here
print('Done') #This last statement is always executed, after the if statement is executed.



while True:
    s = input('Enter something:')
    print('Length of the string is = ', len(s))
    if s == 'quit':
        break
    if len(s) < 5:
        print('Too small')
        continue
    print('Input is of insufficient length')
print('Done')



def total(a=5, *numbers, **phonebook):
    print('a',a)
    for single_item in numbers:
        print('single_item', single_item) #iterate through all the items in tuple
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)
total(10,1,2,3,5, Jack=78461 ,John= 126165, inge=565489)



import sys
print('The command line arguments are:')
for i in sys.argv:
    print(i)
print('\n\nThe PYTHONPATH is ', sys.path,'\n')



#importing the system files
import sys
dir(sys) #get names of attributes in sys module
['__displayhook__', '__doc__', 'argv', 'builtin_module_names', 'version', 'version_info'] #Only few entries shown here
dir()
['__builtins__', '__doc__', '__names__', '__package__', 'sys'] #get names of attributes for current module
a = 5 #create a new variable 'a'
dir()
['__builtins__', '__doc__', '__names__', '__package__', 'sys', 'a']
del a
dir()
['__builtins__', '__doc__', '__names__', '__package__', 'sys']


#This is the program of your whistlist
shoplist = ['apple', 'mango', 'carrot', 'banana']
print('I have ',len(shoplist), 'items to purchase.')

print('These items are:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is ', shoplist)

print('The first item I will buy is ', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the ', olditem)

print('My shopping list is now', shoplist)

#This is the programm where you get what you want
hacktools = ['laptop', 'smartphone', 'wifi pineapple', 'alexa', 'Sony Television']
print('I have to buy these',len(hacktools), 'hacktools.')

print('These items are:', end=' ')
for items in hacktools:
    print(items, end= ' ')

print('I also want to but sharkjack')
hacktools.append('sharkjack')
print('Now my new list for hacktools is: ', hacktools)

print('I will sort my list now')
hacktools.sort()
print('Now my sorted list looks like', hacktools)

print('The first item I will buy is:', hacktools[0])
olditem = hacktools[0]
del hacktools[0]
print('I bough the ', olditem)
print('My wishlist is now :', hacktools)


# I would recommend always using parantheses
# To indicate start and end of tuple
# Even though parantheses are optional.
# Explicit is better than implicit.

zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is ', len(zoo))

new_zoo ='monkey', 'camel', zoo #parantheses are not required but are good idea
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animals brought from old zoo is ', new_zoo[2][2])
print('Number of animals in the new zoo is', len(new_zoo)-1+len(new_zoo[2]))



ab = {
    'Prathamesh' : 'pdshntsharda@gmail.com',
    'LazyBear'   : 'apibagalprathamesh@protonmail.com',
    'Hemlata'    : 'hemlatadbagal@gmail.com',
    'Deepak'     : 'djbagal@gmail.com',
    'Soham'      : 'sohamkulkarni1a2b3c@gmail.com',
    'Neha'       : 'smartnehurock565@gmail.com', \
    'Swaroop'    : 'swaroop@swaroopch.com',
    'Larry'      : 'larry@wall.org',
    'Matsumoto'  : 'matz@ruby-lang.org',
    'Spammer'    : 'spammer@hotmail.com'
}
print("Swaroop address is ", ab['Swaroop'])
del ab['Spammer'] # Deleting a key value pair
print('\n There are {} contacts in adress-book list.\n'.format(len(ab)))
for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))
ab['Nupur'] = 'nupimay@gmail.com'
if 'Nupur' in ab:
    print("Nupur address is", ab['Nupur'])




shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'Prathamesh'

#Indexing or 'Subscription' operation #
print('item 0 is ',shoplist[0])
print('item 1 is ',shoplist[1])
print('item 2 is ',shoplist[2])
print('item 3 is ',shoplist[3])
print('item -1 is ',shoplist[-1])
print('item -2 is ',shoplist[-2])
print('Character 0 is ', name[0])

#Slicing on a list #
print('Item 1 to 3 is ', shoplist[1:3])
print('Item 2 to end is ', shoplist[2:])
print('Item 1 to -1 is ', shoplist[1:-1])
print('Item started to end is ', shoplist[:])

#Slicing on a string#
print('Character 1 to 3 is ', name[1:3])
print('Character 2 to end is ', name[2:])
print('Character 1 to -1 is ', name[1:-1])
print('Character start to end is ', name[:])


print('Simple Assignment')
shoplist = ['Apple', 'mango', 'carrot', 'banana'] # mylist is just another name pointing to the same object
mylist = shoplist
# I purchased the first item , so I remove it from the list
del shoplist[0]
print('shoplist is', shoplist)
print('mylist is ', mylist)

#Notice that both shoplist and mylist both print
# The same list without the 'apple' confirming that
# they point to the same object

print('Copy by making a full slice')
# make a copy by doing a full slice
mylist = shoplist[:]
# Remove first item
del mylist[0]

print('shoplist is ', shoplist)
print('mylist is ', mylist)
#notice that now the two lists are different



# This is a string object
name = 'Swaroop'

if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')

if 'a' in name:
    print('Yes, it contains the string "a"')

if name.find('war') != -1:
    print('Yes, it contains the string "war"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))



import os
import time
# 1. The files and directories to be backed up are
# specified in a list.
# Example on windows:
# source = ['"C:\\My Documents"']
# Example on Mac OS X and Linux:
source = ['/Users/pdshn/notes']
#Notice we have to use double quotes inside a string
# for names with spaces in it. We could have also used
# a raw string by writing [r'C:\My Documents']

#2. The backup must be stored in a
# main backup directory
# Example on Windows:
# target_dir = 'E:\\Backup'
# Example on Mac OS X and Linux:
target_dir = '/Users/pdshn/backup'
# Remember to change this to which folder you will be using

# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time.
target = target_dir + os.sep + \
    time.strftime('%Y%m%d%H%M%S') + '.zip'

# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)   # Make directory

# 5. We use the zip command to put the files in a zip archive
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))


# Run the backup
print('zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('SUCCESSFUL BACKUP to ',target)
else:
    print('Backup FAILED')



####################################################  My first programm
Number = int(input("Enter a number"))
print("Your number is :", Number)
square = Number*Number
print("Square root of the number is =", square)
Cube = Number*Number*Number
print("Cube   root of the number is =", Cube)
#another method
Number = int(input("Enter a number"))
for i in range (1,Number):
    Cube = i*i*i
    print("\n Cube root of the number",i, "is = \n", Cube)



a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))
d = int(input("Enter the forth number : "))
if a>b and a>c and a>d:
    print("The biggest number is =",a)
elif b>a and b>c and b>d:
    print("The biggest number is =",b)
elif c>a and c>b and c>d:
    print("The biggest number is =",c)
elif d>a and d>b and d>c:
    print("The biggest number is =",d)



for i in range (1,100):
    if i % 3 == 0 and i % 5 == 0:
        continue
    print("Values divisible by 3 and 5", i)

Number = int(input("Enter a Number :"))
if Number<=1:
    print(Number,"is not a prime number")
else:
    for i in range(2,Number):
        if Number%i == 0:
            print(Number, "is not a prime number")
            break
    else:
        print(Number, "is a prime number")


for a in range (10):
    for b in range (10-a):
        print("$", end="")

print()

a = int(input("Enter a Number: "))
for i in range(2,a):
    if a % i ==0:
        print("Not Prime")
        break
else:
    print("Prime")




from array import *
vals = array('i',[5,6,-8,9,10])

newarr = array(vals.typecode, (a*a for a in vals))
newarr.reverse()
i = 0
while i<len(newarr):
    print(newarr[i])
    i+=1


from array import *
arr = array('i', [])
n = int(input("Enter the length of the array :"))
for i in range(n):
    x = int(input("Enter the Values :"))
    arr.append(x)

print(arr)

vals = int(input("Enter the value for search :"))
b=0
for a in arr:
    if a == vals:
        print(b)
        break
    b+=1
print(arr.index(vals))

from numpy import *
arr = array([9,5,8,3,4,2])
arr1 = array([5,2,1,3,4,6])
arr2 = ([])
k = 0
for i in arr:
    j=i + arr1[k]
    arr2.append(j)
    k+=1
print(arr2)


from numpy import *
arr = array([9,5,8,3,4,2])
max = arr[0]
n = len(arr)

for i in range(1,n):
    if arr[i]>max:\
        max = arr[i]
print(max)

from numpy import *
arr1 = array([
                [2,3,4,5,0,77],
                [5,6,7,8,66,44]
            ])
arr2 = arr1.flatten()
arr3 = arr2.reshape(2,2,3)
print(arr3)

from numpy import *
m = matrix('1 2 3;4 5 6;7 8 9')
print(diagonal(m))


def person(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)

person('Prathamesh',age=20, city='Pune', mob = 8379085845)


a = 10
print(id(a))
def something():
    a = 8
    x = globals()['a']
    print(id(x))
    print(a)
    globals()['a']=20

something()
print(a)

def count(l):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even+=1
        else:
            odd+=1
    return even,odd
lst = [20,25,30,35,40,45,50]
even,odd = count(lst)
print("Even :{} and Odd : {}".format(even,odd))


#take 10 names from the users and then count and display number of users who has length more than 5 letters


def fib(n):
    a = 0
    b = 1
    if n<0:
        print('Invalid number')
    elif n ==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a +b
            a = b
            b = c
            if c > 100:
                break
            print(c)
fib(100)



def div(a,b):
    print(a/b)
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner
div1 = smart_div(div)
div1(2,4)




def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return f
x = 6
result = fact(x)
print(result)




import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
i = 0
def greet():
    global i
    i+=1
    print("Hello", i)
    greet()
greet()

def fact(n):
    if (n==0):
        return 1
    return n * fact(n-1)
result = fact(9)
print(result)






def square(a):
    return a*a
result = square(8)
print(result)


f = lambda a,b: a+b
result = f(8,5)
print(result)




def is_even(n):
    return n%2==0
nums = [3,2,4,5,6,8,2,5,9,78,2]
evens = list(filter(is_even,nums))
print(evens)




nums = [3,2,4,5,6,8,2,5,9,78,2]
evens = list(filter(lambda n : n%2==0,nums))
print(evens)



from functools import reduce
def add_all(a,b):
    return a+b
nums = [3,2,4,5,6,8,2,5,9,78,2]
evens = list(filter(lambda n : n%2==0,nums))
doubles = list(map(lambda n : n*2,evens))
sum = reduce(lambda a,b : a+b,doubles)
print(sum)



from functools import reduce
nums = [3,2,4,5,6,8,2,5,9,78,2]
evens = list(filter(lambda n : n%2==0,nums))
doubles = list(map(lambda n : n*2,evens))
print(doubles)
sum = reduce(lambda a,b : a+b,doubles)
print(sum)



def div(a,b):
    if a<b:
        a,b = b,a
    print(a/b)
div(2,4)





from calc import add
def func1():
    print("its fun1")

def func2():
    print("its fun2")

def main():
    func1()
    func2()

main()


class Computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is =", self.cpu ,self.ram)
comp1 = Computer('i7 Processor', 8)
comp2 = Computer('i5 Processor', 16)

comp1.config()
comp2.config()






class Computer:
    def __init__(self):
        self.name = "Prathamesh"
        self.age = 21
    def update(self):
        self.age = 28
c1 = Computer()
c2 = Computer()
c1.update()
print(c1.name)
print(c2.age)



class Cars:
    wheels = 4
    def __init__(self):
        self.company = "Mercedez-Benz"
        self.mil = 22
c1 = Cars()
c2 = Cars()
c1.mil = 9
Cars.wheels = 6
print(c1.company, c1.mil, c1.wheels)
print(c2.company, c2.mil, c2.wheels)


class students:
    School = 'Stanford university'
    def __init__(self,m1,m2,m3):
        if __name__ == '__main__':
            self.m1 = m1
            self.m2 = m2
            self.m3 = m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod
    def info(cls):
        return cls.School
    @staticmethod
    def classname():
        print("This is student class in abc module")

    def get_m1(self):
        return self.m1
    def set_m1(self,value):
        self.m1 = value
s1 = students(88,95,64)
s2 = students(81,45,68)
print(s2.avg())
print(students.info())
print(students.classname())






class Students:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
    def show(self):
        print(self.name, self.rollno)
        self.lap.show()
    class Laptop:
        def __init__(self):
            self.brand = 'Hp'
            self.processor = 'i7'
            self.ram = '8GB'
        def show(self):
            print(self.brand, self.processor, self.ram)
s1 = Students('Prathamesh',134)
s2 = Students('Millie',135)

s1.show()
lap1 = Students.Laptop()









class A:
    def feature1(self):
        print("feature one is working")
    def feature2(self):
        print("feature two is working")
class B(A):
    def feature3(self):
        print("feature three is working")
    def feature4(self):
        print("feature four is working")
a1=A()
a1.feature1()
a1.feature2()
b1=B()
b1.
b1.feature3()
b1.feature4()



class pycharm:
    def execute(self):
        print("Compiling")
        print("Running")
class Myeditor:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Probe Check")
        print("Compiling")
        print("Running")
class Laptop:
    def code(self,ide):
        ide.execute()
ide = Myeditor()
lap1 = Laptop()
lap1.code(ide)








class Students:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def sum(self,a=None,b=None,c=None):
        s = 0
        if a!=None and b!=None and c!=None:
            s = a + b + c
        elif a!=None and b!=None:
            s = a + b
        else:
            s = a
        return s

s1 = Students(88,56)
print(s1.sum(5))







class A:
    def show(self):
        print("A is show")
class B(A):
    pass
a1 = B()
a1.show()






from abc import ABC, abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        print("Running")
class Laptop(Computer):
    def process(self):
        print("Its Running")
class whiteboard():
    def write(self):
        print("Its writing")
class programmer:
    def code(self):
        print("I am a coder")
com1 = Laptop()
com1.process()
prog = programmer()
prog.code()
write = whiteboard()
write.write()
#com = Computer()
#com.process()








class topten:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
            val = self.num
            self.num += 1
            return val
values = topten()
print(next(values))
for i in values:
    print(i)








class topten:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration
values = topten()
print(next(values))
for i in values:
    print(i)












def topten():
    yield 5
    yield 15
    yield 25
    yield 35
    yield 45
    yield 55
values = topten()
print(values.__next__())
print(values.__next__())
for i in values:
    print(i)







def topten():
    n = 1
    while n<=30:
        sq = n*n
        yield sq
        n +=1
values = topten()
for i in values:
    print(i)







a = 9
b = 2
try:
    print("Resource Open")
    print(a/b)
    k = int(input("Enter a number"))
    print(k)
except Exception as error:
    print("Hey get the fuck out of here.", error ,"is the error")
finally:
    print("Resource Closed")
print("Bye")







from time import sleep
from threading import *
class Hello(Thread):
    def run(self):
        for i in range(4):
            print("Hello")
            sleep(2)
class Hi(Thread):
    def run(self):
        for i in range(4):
            print("Hi")
            sleep(2)
o1 = Hello()
o2 = Hi()
o1.start()
sleep(0.1)
o2.start()
o1.join()
o2.join()
print("Bye")








from time import sleep
from threading import *
class Hello(Thread):
    def run(self):
        for i in range(4):
            print("Hello")
            sleep(2)
class Hi(Thread):
    def run(self):
        for i in range(4):
            print("Hi")
            sleep(2)
o1 = Hello()
o2 = Hi()
o1.start()
sleep(0.1)
o2.start()
o1.join()
o2.join()
print("Bye")






f = open('calc.py','r')
f1 = open('abc', 'w')
f1.write("Something")
f1.write(" I don't know.")
for data in f:
    f1.write(data)