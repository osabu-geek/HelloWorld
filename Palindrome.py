
print()
word = input("Please enter any word here: ")
length_of_word = len(word)
section_word = int(length_of_word/2)
k = section_word

if word[0:k] == word[-1:-k - 1:-1]:
    print(word, "The word entered is palindrome.")
    print()
    print("It means that the word can pronounced in the forward or reverse direction.")
else:
    print(word, "The word is not a palindrome.")
    print()
    print("It means that the word can be pronounced correctly in the forward direction only.")
