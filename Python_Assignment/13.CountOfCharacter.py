#Write a Python program to count the occurrences of each word in a given sentence

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