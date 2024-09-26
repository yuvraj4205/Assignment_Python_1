#Write a Python function to reverses a string if its length is a multiple of 4.

def reversestring(string):
    if len(string)%4==0:
        return string[::-1]
    else:
        return string
    
userstring=input("Enter a string : ")
result=reversestring(userstring)
print("Resulting string :",result)