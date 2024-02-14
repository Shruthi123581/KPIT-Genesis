'''
fin = open('C:/Users/SHRUTHIB/Documents/Python/words.txt')
for line in fin:
    #word = line.split()
    for letter in line.split():
        if(len(letter)>8):
            print(letter)
'''

fin = open('C:/Users/SHRUTHIB/Documents/Python/anagram.txt')
for line in fin:
    word = line.strip()
    print(word)
    
