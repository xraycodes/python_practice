# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}
 
# Text string
text = "Later in the course, you'll see how to use the collections Counter class."
 
# Your code goes here ...

for letter in text:
    lowercase = letter.casefold()
    if lowercase.isalnum():
        if lowercase in word_count:
            word_count[lowercase] += 1
        else:
            word_count[lowercase] = 1
 
# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)
