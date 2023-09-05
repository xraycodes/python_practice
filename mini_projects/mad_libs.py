text = 'story.txt'

with open(text,) as f:
    story = f.read()

story_list = story.split()
replacement_words = []

for word in story_list:
    if word.startswith('<'):
        replacement_words.append(word)

for word in story_list:
    print(word, end = ' ')
    if word in replacement_words:
        input_replacement = input(f"\nWhat word would you like to replace {word} with ")
        if word in story_list:
            word = input_replacement
   
print(story_list)