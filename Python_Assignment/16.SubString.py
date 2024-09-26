'''Write a Python program to find the first appearance of the substring 
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the 
whole 'not'...'poor' substring with 'good'. Return the resulting string.'''

text="The lyrics is poor from the beginning to the end, not worth listening."

poor_index=text.find('poor')
not_index=text.find('not')

if poor_index!=-1 and not_index!=-1 and poor_index<not_index:
    good_index=poor_index
    text=text[:good_index] + 'good' + text[not_index + 3:]

print(text)