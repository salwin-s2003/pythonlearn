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