'''Write a Python program to sum of three given integers. However, if 
two values are equal sum will be zero.'''

a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
c=int(input("Enter a number : "))

if a==b or b==c or a==c:
    sum=0
else:
    sum=a+b+c

print("The sum is : ",sum)