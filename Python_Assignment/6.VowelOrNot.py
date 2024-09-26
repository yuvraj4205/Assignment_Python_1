'''Write a Python program to test whether a passed letter is a vowel or 
not.'''

letter=input("Enter an Alphabet : ")

letter=letter.lower()
letter=letter.upper()

if letter in ['a','e','i','o','u','A','E','I','O','U']:
    print("The alphabet is Vowel.")
else:
    print("The alphabet is consonant.")