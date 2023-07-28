def removeprefix(string: str, prefix: str) -> str:
    if string.startswith(prefix):
        return string[len(prefix):]
    else:
        return string[:] #return copy of 'string'
    
def removesuffix(string:str, suffix: str) ->str:
    if suffix and string.endswith(suffix): #suffix=' ' should not call string[:-0]
        return string[:-len(suffix)]
    else:
        return string[:]

filename = 'Jabberwocky.txt'
with open(filename) as poem:
    first = poem.readline().rstrip()

print(first)

chars = "T'awsebv"
# no_apostrophe = first.strip(chars)
# print(no_apostrophe)

for character in first:
    if character in chars:
        print(f"Removing {character}")
    else:
        break

print('*' * 80)

for character in first[::-1]: #process backwards
    if character in chars:
        print(f"Removing {character}")
    else:
        break

print('*' * 80)

#This only works after python 3.9
# twas_removed = first.removeprefix("'Twas")
# print(twas_removed)
# toves_removed = first.removesuffix("Toves")
# print(toves_removed)

twas_removed = removeprefix(first, "'Twas")
print(twas_removed)

toves_removed = removesuffix(first, 'toves')
print(toves_removed)