fin = open('C:/Users/SHRUTHIB/Documents/Python/words.txt')

def anagram1(inp):
    dict1 = {}
    for i in input:
        key = ''.join(sorted(i))