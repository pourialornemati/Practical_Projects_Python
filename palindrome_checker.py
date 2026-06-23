word = input("Enter a word: ")

# create an empty string to store the reversed word
reverse_word = ""

# loop through each character in the word
for ch in word:
    # add each character to the front of reverse_word
    reverse_word = ch + reverse_word

# check if the original word and reversed word are the same
if word == reverse_word:
    print("This word is a palindrome")
else:
    print("This word is NOT a palindrome")