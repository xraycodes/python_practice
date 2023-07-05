d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

# Good way to initialize a dictionary in the beginning, can change the value afterwards
new_dict = dict.fromkeys(pantry_items)
print(new_dict)

# Rarely used. .keys may make it clearer, prints out the key in list
keys = d.keys()
print(keys)


# for items in d.keys():
    print(items)

#using .values() method. Useful to check if value exists in dictionary.
v = d.values()
print(v)


#Updating methods
d2 = {
    7: "lucky seven",
    10: "ten",
    3: "this is the new three"
}

d.update(d2)
for key, value in d.items():
    print(key,value)

print()

d.update(enumerate(pantry_items))
for key, value in d.items():
    print(key, value)
