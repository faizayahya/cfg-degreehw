THEORY QUESTIONS: 

1) What is Python and what are its main features?

One of the most dynamic and adaptable programming languages currently used in the industry today is Python. Python is a high level, open source programming language that has been in operation since the 1990s and is powerful, interactive and object-oriented. 

Python offers a wide range of functionality as a programming language. Among Python's main features are that it is easy to read and code meaning anyone can learn. Another key feature is it’s object-oriented approach. This simply means that Python understands the idea of class and object encapsulation, enabling long-term program efficiency.

Another feature is that it is an integrated language by nature. As a result, the Python interpreter runs codes line by line. We don't need to build Python code, unlike other object-oriented programming languages, which makes the debugging process considerably simpler and more effective. Another benefit of doing this is that the Python code is quickly transformed into byte-code, an intermediate form that is easier and faster to execute. 

2) Discuss the difference between Python 2 and Python 3

The Python 3 programming language, which was introduced in December 2008, was the replacement and upgrade for Python 2 that was released in 2000.
Many syntax changes were made, as well as a substantially larger standard library, to improve Python's usability and programming experience. These modifications mean that Python 3 is not exactly backward compatible with Python 2.

One of the most fundamental differences between Python 2 and 3 is the Print statement. To print values on the terminal in Python 2, use the special statement known as print. This indicates that no parentheses are required when using the print statement. Python 3's print, in contrast, is a function that must be called within parentheses.

Python 2 users can use the more recent print function by importing print function from the future module.

The Division of Integers is another significant distinction between the two. When you divide two integers, you always receive a float number.

If we use the "/" operator, Python2 will by default divide an integer. However, Python 3 divides the operands of the "/" operator using floating point operations. Python 3 still supports integer division with the double " // " operator.  



3) What is PEP 8?

PEP 8 is a document written in 2001 that provides the guidelines and best practices for creating Python code . PEP 8's main objective is to improve the consistency and readability of Python code.

4) In computing, what is a program?

In computing, a program is a sequence or a set of instructions in a programming language for a computer to perform.  A program instructs the computer on how to process data. Programs are created using many types of programming languages such as Python, C++ and Ruby. 

5) In computing, what is a process? 

A process is defined as the set of instructions currently being processed by the computer processor.  An example of this would be in Windows, where you can see each process being run by pressing Task Manager and opening the Processes tab. 

6) In computing, what is a cache? 

In a computing setting, a cache is a chip-based feature that is used to tempo temporarily store something, typically data. This function enables you to access information quickly. This temporary memory, which is also the fastest memory in your computer, houses the data from the programs and files you use the most.

7) In computing, what is a thread and what do we mean by multithreading? 

A thread in computing is the shortest designed sequence of instructions that is being executed.
A style of program execution known as "multithreading" enables the creation of many threads that can run concurrently and independently while sharing process resources. If allocated to their own CPU core, threads may be able to operate in parallel, depending on the hardware.

8) In computing, what are concurrency and parallelism and what are the differences between them?

Concurrency is referred to as the application that performs multiple tasks at the same time. By using a single processing unit, concurrency is a method  that reduces the system's response time. This is accomplished by the central processing unit's (CPU) ability to run processes concurrently, or more often known as context switching.

Parallelism refers to an application where tasks are broken down into smaller sub-tasks and processed in parallel or “seemingly” simultaneously. Using many processors, this allows the system's throughput and computing speed to be increased. It makes it possible for single sequential CPUs to perform many tasks  “seemingly” simultaneously.

9) What is GIL in Python and how does it work?

GIL ensures that there is only one thread of execution able to mutate Python objects at a time. It is a single lock that adds the requirement that the execution of any Python byte code involves obtaining the interpreter lock by creating a single lock on the interpreter itself. 

10) Explain what the following software development principles mean: DRY, KISS, BDUF

The acronym "Don't Repeat Yourself" (DRY) is frequently used by programmers to indicate that software systems are made to automate specific repetitive operations. There are techniques to lessen or entirely get rid of repetition in coding arrays where the same command line is repeated. 

You can apply DRY to Python as follows:

name = 'Faiza'
my_family = ['Faiza', 'Faysal', 'Maria']
if name in my_family:
    print 'yes.'

The phrase "Keep it Simple, Stupid" (KISS) was  coined to convey to the engineers the need of keeping a design straightforward.
This idea is crucial to software development. Programmers are often urged to avoid writing code that is overly complex or makes it difficult to understand. The goal is to program only what is necessary.

BDUF is an approach where the design is completed before the implementation begins. This idea is crucial to software development. BDUF is an acronym for Big Design Up Front. 

11) What is a garbage collector in Python and how does it work?

The garbage collector in Python keeps track of all objects in memory. Python automatically deletes objects (class instances or built-in types) to clear up memory space. Garbage Collection is the method used by Python to regularly release and reclaim memory blocks that are no longer needed.

12) How is memory managed in Python?

Memory is managed by the Heap data structure in Python. This holds the objects and other data structures that are used in the program. Through the use of API functions, the Python memory manager controls the allocation and deallocation of heap memory space.

13) What is a Python module? 

A file containing Python definitions and statements is referred to as a module. We utilize modules to break down complicated programs into smaller, more manageable pieces. A module is a file that contains Python code; an example of this would be:
a file with the name example would be saved as example.py and this would be a module.

14) What is a docstring in Python?

In Python, docstrings are strings that are used right after the definition of a module, class, function, or method so that programmers may understand what it does without having to look into the details of the implementation. This can be accessed by using the __doc__ attribute.

15) What are pickling and unpickling in Python? Give example(s).

Pickling is the process of converting Python objects to byte streams in Python. Pickling involves serializing the Python object structure. Whereas Unpickling is the process of getting the original Python objects from the pickle file's stored string representation.

You can only pickle and unpickle once you have used the following command −
import pickle

An example of pickling is: 

import pickle
myexample = ['a', 'b', 'e', 'f']
with open('datafile.txt', 'wb') as fh:
  pickle.dump(myexample, fh)

In the code above, “myexample” has four elements in it, we can open the file in “wb” instead of “w”. With this a new file called “datafile.txt” is made, this converts all of the data in myexample into the byte stream. You can unpickle this by inputting the following code: 

myexample = open ("filename", "rb")
myexample = pickle.load(myexample_pickle)
print(myexample_contents)

16) What tools exist to help find bugs or perform static analysis in Python? 

The tools that aid in finding Python issues include Pychecker and Pylint.  Pychecker is a free static analysis tool that highlights the complexity and style of defects in source code and finds them in the code.

Pylint is extremely configurable and functions as a special program to regulate faults and warnings.   It measures the length of each line of code and verifies the variable names according to the style of the project.  It is able to run independently and is compatible with Python IDEs like Pycharm, Spyder and Eclipse.

17) How are arguments passed in Python (by value or by reference)? Give example(s).

The "Call-by-Object" method, also known as "Call by Object Reference"  is used by Python to pass arguments. All arguments are passed by reference. It means that if you alter the meaning of a parameter within a function, the change is reflected in the calling function.

my_family={'Faiza':26,'Mustafa':25,'Ayman':9,'Maria':27}
def test(my_family):
  new={'Faysal':17}
  my_family.update(new)
  print("Inside the function",my_family)
  return
test(my_family)
print("outside the function:",my_family)

18) What are Dictionary and List comprehensions in Python? Give example(s).

List comprehensions are built using bracketed expressions that are followed by a for clause. Similar to List Comprehension, Python also allows dictionary comprehensions.This can be done by using the dict() syntax and can only be used for dictionaries. You can initialise a dictionary in Python by doing the following: 


dict = {'orange': 'fruit', 'cucumber': 'vegetable', 'cupcake': 'dessert'}
dict['nuts'] = 'snack'
print(dict['orange'])

An example of a List Comprehension is as follows: 


fruits_list = ["banana", "apple", "orange", "pineapple", "blueberry"]
newlist = [x for x in fruits_list if "a" in x]
print(newlist)

19) What is a namespace in Python?

A namespace can be compared to a dictionary, where the keys are the object names and the values are the actual objects. It provides a unique name for each object in Python. 

20) What does pass mean in Python?

The pass statement is utilised as a placeholder for future code. Nothing happens when this statement is executed and it is a way to avoid getting an error where empty code is not allowed. Examples of where empty code would not be allowed would be: function definitions, class definitions and loops. 

21) What is a unit test, and what does unittest mean in Python?

When testing software, a technique known as unit testing is used to look at the small testable pieces of code and checks them for proper operation. Unit testing allows us to ensure that every aspect of the code, including helper functions that may not be visible to the user, works correctly and as intended.

22) What is slicing in Python? 

The ability to access portions of sequences like strings, tuples, and lists in Python is known as slicing. They can also be used to change or remove items from mutable sequences such as lists.

23) What does a negative index represent in Python? 

In the Python programming language, negative indexing of arrays is possible unlike other programming languages. As a result, an array's last and second-last elements can be found by using the index values -1 and -2.  The negative indexing begins at the end of the array. This does mean that the last element of an array is also the first element in the negative indexing, meaning it would be -1.

24) How can ternary operators be used in python? Give example(s). 

Ternary operators, commonly referred to as conditional expressions, are operators that assess something dependent on whether a condition is true or false. This was introduced in version 2.5 of Python. It enables single-line condition testing as opposed to multiline. 
a, b = 7, 8
if a>b:
  print("a")
else:
  print("b")
x, y = 7, 8
print("a" if a> b else "b")
Output = b
b

25) What are *args and **kwargs in Python, and why might we use them?

*args allow us to collect the positional arguments that have not been defined explicitly. This is similar to **kwargs however, it is for keyword arguments. This allows you to pass a function with a number of arguments. 

26) How are range and xrange different from one another? (Both Python 2 and Python 3 are relevant here.)

The Python methods range() and xrange() can be used to iterate a specified number of times in for loops. There is no xrange in Python 3, although the range function functions like xrange in Python 2.

27) What is Flask and what can we use it for?

With the help of help of lightweight Python web frameworks such as Flask we can utilise tools and features that allow making a web application in Python easier.  It provides flexibility to developers and is a more approachable framework for beginning developers because you can easily create a web application with only a single Python file.

28) What are clustered and non-clustered indexes in a relational database?

A clustered index is an index that specifies the physical order of table records stored in a  database.  There can only be one clustered index per table put in one order because there is only one possible way to store the data.  Whereas A non-clustered index doesn’t sort the physical data inside the table. A non-clustered index is stored in one location and the table data is stored in another location. 

29) What is a ‘deadlock’ in a relational database?

A deadlock in a database occurs when many transactions are waiting for each other to release locks. For instance, Transactions may have a lock on some rows in another table such as Accounts that require updating some of the rows in the Orders table to be completed.

30) Livelock is a condition that happens when two or more programs change their states repeatedly without progressing. When two processes conflict with each other's states and cannot progress because both are changing the states at the same time, it is considered to be in livelock. 

STRING METHODS: 

Capitalize - This function copies the original string and changes the first character to an uppercase capital letter while leaving the rest of the characters in lowercase.

This function copies the original string and changes the first character to an uppercase capital letter while leaving the rest of the characters in lowercase.

This returns the string as all lowercase. 
name = "faiza"
print(name.capitalize())
Result = Faiza


name = "Faiza"
x = name.casefold()
Result = faiza 


()casefold() - This returns the string as all lowercase.  

name = "Faiza"
x = name.casefold()
Result = faiza 



center() - This allows the string to align to the centre by using a specified character as a fill.

name = "Faiza"
x = name.center(10)
print(x)

This would take up the space of 10 characters and have the name Faiza in the middle.


count() -  This function returns the number of times an element appears in a list. 

name = "my name is Faiza, my name is Faiza"
x = name.count("Faiza")
print(x)
Result = 2


endswith() - Returns a true answer if the string ends in the mentioned suffix. If it isn’t then it will return as false. 

message = 'I love apples'
print(message.endswith(apples))
Result = True


find() - The integer value returned by the find() function is: If the substring appears anywhere in the string, it returns the index of the first instance. This returns -1 if the value is not found.  

name = "Hello, my name is name."
x = name.find("e")
print(x)
Result = 1


format() - This is used as a placeholder, it formats the specific value and inserts them inside the string. The placeholder is defined by using the {} 

txt = "My name is {fname} and I am {age}".format(fname = "Name", age =  26)
print(txt.format(an = 4))
Result = My name is Name and I am 26

index() - This returns the index of the first occurrence of a given element in the list.

txt = "Hi, this is Python."
x = txt.index("this")
print(x)
Result = 4


isalpha() - This string returns as True if all the characters are alphabetic letters (a-z).

txt = "BBC"
x = txt.isalpha()
print(x)
Result = True



isdigit()  - Returns as True if all of the characters are all digits. If not it will return as False. 

txt = '244'
print(txt.isdigit())
Result = True


islower() - Returns as True if all of the characters are lowercase If not it will return as False. 

txt = "BB 1"
x = txt.islower()
print(x)
Result = False


isnumeric() - isnumeric() is a string that returns as  True if every character is a number (0-9). 

txt = "111"
x = txt.isnumeric()
print(x)
Result = True


istitle() - If every word in a text begins with an uppercase letter the istitle() method returns as True. If not it returns False. 

txt = "Hi This Is Python!"
x = txt.istitle()
print(x)
Result = False 

isupper() - If all of the characters are capitalised, the isupper() method returns True. If not, it returns False. 

txt = "HI THIS IS PYTHON!"
x = txt.isupper()
print(x)
Result = True


join() - The join() method unites all of the elements in an iterable and joins them into a single string. 

text = ['Hi', 'this', 'is', 'Python']
print(' '.join(text))
Result = Hi this is Python


lower() - This returns the string was all uppercase to lowercase.  

txt = 'HI, THIS IS PYTHON'
print(txt.lower())
Result = hi this is python


lstrip() - This returns a copy of the string where all of the leading characters have been removed.  

txt = '   hi there     '
print(txt.lstrip())
Result = hi there


replace() - The replace() method substitutes one phrase for another. 

txt = "I like coding"

x = txt.replace("coding", "food")

print(x)
Result = I like food


rsplit() - The Python String rsplit() function returns a list of strings after splitting it, starting from the right.  

txt= 'wow apples!'
print(txt.rsplit())
Result = ['wow', 'apples!']


rstrip() - This removes any whitespace at the end of a string.  

txt = 'Hi Hi      '
result = txt.rstrip()
print(result)
Result = Hi Hi 


split() - This allows you to split a string into a list.  

txt = "hi welcome python"
x = txt.split()
print(x)
Result = ['hi', 'welcome', 'python']
 

splitlines() - Similar to split(), this splits a string into a list but the splitting is done at the line breaks.  

txt = 'I\nam\nQueen\nof\nPython.'
x = txt.splitlines()
print(x)
Result = ['I', 'am', 'Queen', 'of', 'Python.']
 

Startswith - Startswith is a method that returns as True if the string in the character starts with what is specified. If not it will return as False.  

txt = "I am queen of Python."
x = txt.startswith("I")
print(x)
Result = True 
 

() strip()  - Any leading (spaces that are at the start) and trailing (spaces that are at the end) characters are removed using the strip() method. 

txt = '      Hi Hi'
result = txt.strip()
print(result)
Result = Hi Hi 


swapcase() - All upper case letters are returned as lower case and vice versa using swapcase(). 

txt = "I am queen of PYTHON"
x = txt.swapcase()
print(x)
Result = i AM QUEEN OF python

 
title() - Title() returns a string in which the first character of each word is capitalised. Such as a title or a header. 

txt = "I am queen of python"
x = txt.title()
print(x)
Result = I Am Queen Of Python


upper() - This returns a string all in uppercase.  

txt = "I am queen of python"
x = txt.upper()
print(x)
Result = I AM QUEEN OF PYTHON
 
LIST METHODS:
append() - This function adds a new item to the end of the list. 

Colours = ['Pink', 'Purple', 'Yellow']
Colours.append('Orange')
print(Colours)
Result = ['Pink', 'Purple', 'Yellow', 'Orange']


clear() - This removes all of the items from a list.  

numbers = ['1', '2', '3', '4']
numbers.clear()
 

copy() - This function creates a copy of the list that was specified. 

numbers = ['1', '2', '3', '4']
numbers.copy()
print(numbers) 

count() - This method returns the number of elements of the given value. 

numbers = [1, 2, 3, 4, 2]
count = numbers.count(2)
print('count:', count)
Result = 2


extend() - The extend() method appends all of the elements of an iterable (list,  string..etc.) to the end of the list.

txt = [2, 4]
txt.extend([5, 6])
print(txt)
Result = [2, 4, 5, 6]


index() - This returns the index of the given element in the list.
plants = ['rose', 'peony', 'lillies']
index = plants.index('lillies')
print(index)
Result = 2


insert() - This returns the index of the given element in the list.

colours = ['pink', 'blue', 'brown']
colours.insert(1, "yellow")
print(colours)
Result = ['pink', 'yellow', 'blue', 'brown']




pop() - This removes the item at the specified index from the list and returns the item that was removed.

even_numbers = [2, 4, 6, 8]
removed = even_numbers.pop(2)
print('Removed:', removed)
print('Updated List:', even_numbers)
Result = [2, 4, 8]


remove() - This removes the first matching element from the list.

even_numbers = [2, 4, 6, 8]
even_numbers.remove(6)
print(even_numbers)
Result = [2, 4, 8]


reverse() - This reverses all of the elements in a list. 

names = ['Jordan', 'Mike', 'Ben']
names.reverse()
print(names)
Result = ['Ben', 'Mike', 'Jordan']


  sort() - This sorts the list by using a default ascending order. 

names = ['Ben', 'Mike', 'Henry']
names.sort()
print(names)
Result = ['Ben', 'Henry', 'Mike']


TUPLE METHODS: 

count() - The built-in Python tuple count() function helps us determine the occurrence of each element in the tuple and returns the number that was counted.  This method looks up a given element in a tuple and returns the number of times it appears there.

atuple = (1, 5, 4, 5, 7, 5, 4, 6, 8, 5)
x = atuple.count(5)
print(x)
Result = 4


index() - The index() function locates the specified element within a tuple and returns the element's position. The first occurrence of the element in the tuple is returned.

letters = ('a', 'b', 'c', 'e', 'u')
index = letters.index('e')
print(index)
Result = 3


DICTIONARY METHODS:

clear() - This removes all items from the dictionary. 

names = {"Ben", "Tom"}
names.clear()
print(names)
Result = set()


copy() - Returns a copy of the dictionary. 

cfgmarks = {'SQL':80, 'Python':81}
copiedcfgmarks = cfgmarks.copy()
print('cfgmarks:', cfgmarks)
print('Copied Marks:', copiedcfgmarks)
Result = cfgmarks: {'SQL': 80, 'Python': 81}
Copied Marks: {'SQL': 80, 'Python': 81}

fromkeys() - Returns a dictionary with the values and keys that were specified. 

x = {'a', 'b', 'c'}
y = 1
mydictionary = dict.fromkeys(x, y)
print(mydictionary)
Result = {'a': 1, 'b': 1, 'c': 1}


get() - This returns the value of the value that was specified. 

crisp = {
 "brand": "Cheetos",
 "flavour": "hot",
}
x = crisp.get("flavour")
print(x)
Result = hot

items() - This returns a list with a tuple for each key-value pair.  

car = {
 "brand": "Mercedes",
 "model": "GLC",
 "year": 2021
}
y = car.items()
car["year"] = 2022
print(y)
Result = dict_items([('brand', 'Mercedes'), ('model', 'GLC'), ('year', 2022)])

 keys() - The keys() method returns a list that contains the dictionaries keys.

car = {
"brand": "Mercedes",
"model": "GLC",
"year": 2021
}
y = car.keys()
print(y)
Result = dict_keys(['brand', 'model', 'year'])


pop()  - This allows you to remove a specified item from the dictionary.

cfggrade = { 'Python': 77, 'MySQL': 72}
element = cfggrade.pop('Python')
print('Popped Marks:', element)
Result = 77


popitem() - The last item that was added to the dictionary is removed using the popitem() method.

car = {
"brand": "Mercedes",
"model": "GLC",
"year": 2021
}
car.popitem()
print(car)
Result = {'brand': 'Mercedes', 'model': 'GLC'}


setdefault() - If the key is in the dictionary, this method allows you to return the value of a key. 

car = {
"brand": "Mercedes",
"model": "GLC",
"year": 2021
}
y = car.setdefault("model", "GLA")
print(y)
Result = GLA

update() - The update() method populates the dictionary with elements from an iterable of key/value pairs or another dictionary object.

cfggrade = { 'Python': 77, 'MySQL': 72}
included_marks = {'Theory':90}
cfggrade.update(included_marks)
print(cfggrade)
Result = {'Python': 77, 'MySQL': 72, 'Theory': 90}


values() - The dictionary's values are listed in the view object and this feature can be used to return a view object.  

cfggrade = { 'Python': 77, 'MySQL': 72}
print(cfggrade.values())
Result = dict_values([77, 72])


SET METHODS: 

add() - This allows you to add a new element to the list. 

car = {
"brand": "Mercedes",
"model": "GLC",
"year": 2021
}
car["colour"] = "black"
print(car)
Result = {'brand': 'Mercedes', 'model': 'GLC', 'year': 2021, 'colour': 'black'}


clear() - This is used to clear all of the elements of a specific set.  

name = {1: "Faiza", 2: "Yahya"}
name.clear()
print(name)
Result = {}


copy() - This returns a copy of the set.  

cfgmarks = {'SQL':80, 'Python':81}
copiedcfgmarks = cfgmarks.copy()
print('cfgmarks:', cfgmarks)
print('Copied Marks:', copiedcfgmarks)
Result = cfgmarks: {'SQL': 80, 'Python': 81}
Copied Marks: {'SQL': 80, 'Python': 81}


difference() - This returns a set that shows the difference between two different sets.  

name = {"John", "Lenon", "Seri"}
last_name = {"Bart", "Ben", "Lenon"}
name = last_name.difference(name)
print(name)
Result = {'Bart', 'Ben'}

intersection() - This returns a set that shows the similarities between two sets or more.  
dict1 = {"Name": "Faiza", "Age" : 26, "School" : "CFG", "City" : "London"}
dict2 = {"Name": "Faiza", "Month": "May", "Work" : "DICE", "City" : "London"}
print ("Original Dict 1: ", dict1)
print ("Original Dict 2: ", dict2)
intersect = {x:dict1[x] for x in dict1
         if x in dict2}
print ("Intersected dict: ", str(intersect))
Result = Original Dict 1:  {'Name': 'Faiza', 'Age': 26, 'School': 'CFG', 'City': 'London'}
Original Dict 2:  {'Name': 'Faiza', 'Month': 'May', 'Work': 'DICE', 'City': 'London'}
Intersected dict:  {'Name': 'Faiza', 'City': 'London'}


issubset()  - If every item in the set is present in the given set, the issubset() method returns True, if not it will return as False.

x = {2, 3, 4}
y = {1, 2, 3, 4, 5}
print(x.issubset(y))
Result = True


issuperset()  - If every item in the supplied set is present in the original set, the issuperset() method returns True if not it will return as False.

X = {2, 3, 4, 5}
Y = {5, 0, 2, 1, 2, 3, 4, 5}
print("A.issuperset(B) : ", X.issuperset(Y))
print("B.issuperset(A) : ", Y.issuperset(X))
Result = A.issuperset(B) :  False
B.issuperset(A) :  True


pop() - This will remove a random item from a given set. 

car = {
"brand": "Mercedes",
"model": "GLC",
"year": 2021
}
car.pop("model")
print(car)
Result = {'brand': 'Mercedes', 'year': 2021}


remove() - Using this you can remove a specified element from the given set.  

dict = ["yellow", "orange", "blue"]
dict.remove("blue")
print(dict)
Result = ['yellow', 'orange']

symmetric_ 
difference() - Symmetric_difference() will return a set that includes all items from both sets but is not present in both of them. 

x = {"yellow", "orange", "blue"}
y = {"banana", "apple", "orange"}
a = x.symmetric_difference(y)
print(a)
Result = {'blue', 'yellow', 'banana', 'apple'}


union() - This returns all of the items from the original set and all of the items from a set that has been specified. Sets can be specified as many times as you want, needing to be separated by commas. 

x = {"yellow", "orange", "blue"}
y = {"banana", "apple", "orange"}
a = x.union(y)
print(a)
Result = {'apple', 'blue', 'orange', 'yellow', ‘banana'}

update() - The update() is a method that updates the current set. This is done by adding elements from another set to the current set.

cfggrade = { 'Python': 77, 'MySQL': 72}
included_marks = {'Theory':90}
cfggrade.update(included_marks)
print(cfggrade)
Result = {'Python': 77, 'MySQL': 72, 'Theory': 90}


FILE METHODS: 

read() - This will return the specified number of bytes out of the file. 

f = open("anexample.txt", "r")
print(f.read())


readline() - This reads one line from the file.

f = open("example.txt", "r")
print(f.readline())
 
readlines() - This returns a list of each line of a file as a list item. 

f = open("example.txt", "r")
print(f.readlines())

write() - This helps write a specific text to the file. 

f = open("anexample.txt", "a")
f.write("\nThank you!")
f.close()

f = open("anexample.txt", "r")
print(f.read())


writelines() - This writes items of a list to the file. 

f = open("example.txt", "a")
f.writelines(["Welcome to my example!", "Thank you."])
f.close()

f = open("example.txt", "r")
print(f.read())
