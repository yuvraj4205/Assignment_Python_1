'''Write a Python program to get a string made of the first 2 and the last 
2 chars from a given a string. If the string length is less than 2, return 
instead of the empty string.'''

def twochars(string):
    if len(string)<2:
        return "String length is less than 2."
    else:
        return string[:2]+string[-2:]
    
userstring=input("Enter a string :")

result=twochars(userstring)
print("String :",result)