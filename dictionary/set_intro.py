numbers = set()

# while len(numbers) < 4: 
#     next_value = int(input("Type number to enter: "))
#     numbers.add(next_value)
# print(numbers)

data = ["blue", "red", "blue", "green", "red", "blue", "white"]
# Create a set from the list, to remove duplicates
unique_data = set(data)
print(unique_data)

#Create a list of unique colours, keeping the order they appeared
unique_data = list(dict.fromkeys(data))
print(unique_data)