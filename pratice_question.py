"""Given two integer numbers, write a Python program to return their product only 
if the product is equal to or lower than 1000. Otherwise, return their sum."""

def product_Sum(num1,num2):
    product=num1*num2
    if product<=1000:
        return "The product of two number is :",product
    else:
        return "The sum of two number is: ",num1+num2
    
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
message,result=product_Sum(num1,num2)
print(f"{message} {result}")

"""Write Python code to iterate through the first 10 numbers and,
 in each iteration, print the sum of the current and previous number.
 Write Python code to iterate through the first 10 numbers and, 
 in each iteration, print the sum of the current and previous number."""

def sum_previous(n):
    number=0
    for i in range(n+1):
        sum = number+i
        print(f"current number {i} previous number {number} the sum is {sum}")
        number=i
n= int(input("Enter a number:"))
sum_previous(n)

"""Write a Python code to accept a string from the user and display characters present at an even index number. """
def even_string(str):
    for i in range(len(str)):
        if i%2==0:
            print(str[i],end = " ")
str=input("Enter a string:")
even_string(str)