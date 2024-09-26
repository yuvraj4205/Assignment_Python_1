#Write a Python program to count the number of characters (character frequency) in a string

freq={}
string=input("Enter a string : ")

for char in string:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1

print("Character Frequencies :")
for char,freq in freq.items():
    print(char,":",freq)