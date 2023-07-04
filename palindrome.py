def is_palindrome(word):
    """
    blahblah
    `int` is good 
    """
    return word[::-1] == word

player_word = input("Choose a word: ").lower()
if is_palindrome(player_word):
    print("{} is a palindrome".format(player_word))
else:
    print("{} is not a palindrome".format(player_word))