def avoids(word,str1):
    for i in str1:
        if i in word:
            return False
    return True
            
print(avoids('shruthi','ashk'))

'''
def avoids(word, forbidden_letters):
    for letter in forbidden_letters:
        if letter in word:
            return False
    return True

def count_words_without_forbidden_letters(filename, forbidden_letters):
    with open(filename, 'r') as file:
        words = file.read().split()

    count_without_forbidden_letters = 0
    for word in words:
        if avoids(word, forbidden_letters):
            count_without_forbidden_letters += 1

    return count_without_forbidden_letters

# Example usage:
filename = 'words.txt'  # Replace with the actual path to your file
forbidden_letters = input("Enter a string of forbidden letters: ")

count = count_words_without_forbidden_letters(filename, forbidden_letters)
print(f"\nNumber of words without forbidden letters: {count}")

'''