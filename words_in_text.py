# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}
 
# Text string
text = "Later in the course, you'll see how to use the collections Counter class."
 
# Your code goes here ...

for letter in text.casefold():
    if letter.isalnum():
        word_count.setdefault(letter, 1) + 1
 
# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)
