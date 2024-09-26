#Write python program that swap two number with temp variable and without temp variable.

a=int(input("Value of A :"))
b=int(input("Value of B :"))
temp=a
a=b
b=temp
print("The Value of A After Swapping : ",a)
print("The Value Of B After Swapping : ",b)
print("*"*40)
a=int(input("Value of A :"))
b=int(input("Value of B :"))
a,b=b,a
print("The Value of A After Swapping : ",a)
print("The Value Of B After Swapping : ",b)