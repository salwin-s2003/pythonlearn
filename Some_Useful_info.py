#to get the address of a variable in memory
a = 100
print(id(a))
b='string'
print(id(b))

c=b
#note in python the variable c is pointing to the same object as b and memory adress is same
print("The address of b :",id(b)," and the address of c :",id(c))

#whenever u wanted to know any type of the variable in python
print(type(a))
"""data types in python
int, float, complex, bool, string, list, tuple, set, dict(Mapping), none, Numeric,range
Numeric is a parent class of int and float . numeric is not a data type in python. numeric has int,float,bool,complex as its child classes.
sequence is a parent class of list, tuple, range, string. sequence is not a data type in python. sequence has list, tuple, range, string as its child classes.
InPyhon there is no char data type.
"""
# to convert float to int 
a = 10.5
b = int(a)
type(b) 
""" In python, the 1 is true and 0 is false"""
print(int(True))
print(int(False))

