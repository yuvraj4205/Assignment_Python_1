'''Write a Python program to get a single string from two given strings, 
separated by a space and swap the first two characters of each string.'''

def swap_and_join(str1,str2):
    
    if len(str1)<2 or len(str2)<2:
        return "Both strings must have at least two characters."
    str1_swapped=str2[2:] + str1[2:]
    str2_swapped=str1[2:] + str2[2:]
    
    result=str1_swapped + " " + str2_swapped
    return result

str1=input("Enter the first string : ")
str2=input("Enter the second string : ")
result=swap_and_join(str1,str2)
print("Resulting string :",result)