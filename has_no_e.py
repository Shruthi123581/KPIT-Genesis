fin = open('C:/Users/SHRUTHIB/Documents/Python/words.txt')
def has_no_e():
    count = 0
    for line in fin:
        for word in line.split():
            
            for i in word:
                
                if 'e' not in word:
                    print(word)
                    count += 1
    percentage = (count*100)/len(line)
    print(percentage)
                
    
                

print(has_no_e())


#Write a program that reads words.txt and prints only the words that have no “e”. Compute the percentage of words in the list that have no “e”.?


'''
def words_without_e(filename):
    with open(filename, 'r') as file:
        words = file.read().split()

    print("Words without 'e':")
    for word in words:
        if 'e' not in word.lower():
            print(word)

    count_without_e = 0
    for word in words:
        if 'e' not in word.lower():
            count_without_e += 1

    total_words = len(words)
    percentage_without_e = (count_without_e / total_words) * 100
    print(f"\nPercentage of words without 'e': {percentage_without_e:.2f}%")

# Replace 'words.txt' with the actual path to your file
words_without_e('words.txt')

'''