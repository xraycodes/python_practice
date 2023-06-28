def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char

    return string[::-1].casefold() == string.casefold()
    

word = input("Whats the word to check? ")
if palindrome_sentence(word):
    print("{} is a palindrome.".format(word))
else:
    print("{} is not a palindrome".format(word))   