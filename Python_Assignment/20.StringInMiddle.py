#Write a Python function to insert a string in the middle of a string.

def middle(original,insert):
    middleindex=len(original)//2
    newstring=original[:middleindex]+insert+original[middleindex:]
    return newstring

str1=input("Enter the original string :")
str2=input("Enter the string to insert :")

result=middle(str1,str2)
print("String :",result)