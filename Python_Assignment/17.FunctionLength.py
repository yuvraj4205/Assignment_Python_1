'''Write a Python function that takes a list of words and returns the length 
of the longest one.'''

def wordlen(words):
    if not words:
        return 0
    return max(len(word) for word in words)

wordlist=["apple","banana","cherry","date"]
result=wordlen(wordlist)
print("The length of the longest word is : ",result)