'''
def is_palindrome(str1):
    if(str1==str1[::-1]):
        print(True)
    else:
        print(False)
    
str2 = input()
is_palindrome(str2)
'''

def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

print(first('shruthi'))
print(last('shruthi'))
print(middle('shruthi'))

