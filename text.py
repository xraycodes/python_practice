
def sentenceMaker(phrase):
    capitalized = phrase.capitalize()
    interrogatives = "how", "what", "why"
    if phrase.startswith(interrogatives):
        return (capitalized + '?')
    else:
        return (capitalized + '.')

inputs = []
while True:
    user_input = input("Say something: ")
    if user_input == '/end':
        break
    else:
        inputs.append(sentenceMaker(user_input))

print(" ".join(inputs))