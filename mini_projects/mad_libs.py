text = 'story.txt'

with open(text,) as f:
    story = f.read()

# words = set()
# start_of_word = -1

# target_start = "<"
# target_end = ">"

# for index, char in enumerate(story):
#     if char == target_start:
#         start_of_word = index
    
#     if char == target_end and start_of_word != -1:
#         word = story[start_of_word: index + 1]
#         words.add(word)
#         start_of_word = -1

# answers = {}

# for word in words:
#     answer = input(f"Enter a word for {word}: ")
#     answers[word] = answer

# for word in words:
#     story = story.replace(word, answers[word])

# print(story)
    





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
            story = story.replace(word, input_replacement)
   
print(f'\n {story}')