# Capital indexes
# Write a function named capital_indexes. The function takes a single parameter, which is a string.
# Your function should return a list of all the indexes in the string that have capital letters.

# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
def capital_indexes(string):
    empty_list = []
    for index, char in enumerate(string):
        if char == char.upper():
            empty_list.append(index)
    return empty_list

    
capital_indexes("hello")


################
# Middle letter
# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter.
#If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".

def mid(string):
    if len(string) % 2 == 0:
        return ""
    else:
        half = len(string) // 2
        return string[half]

################
# Online status
# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.
# For example, consider the following dictionary:
# statuses = {
#     "Alice": "online",
#     "Bob": "offline",
#     "Eve": "online",
# }
# In this case, the number of people online is 2.
# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
# Your function should return the number of people who are online.

def online_count(dictionary):
    count = 0
    for values in dictionary.values():
        if values == 'online':
            count += 1
    return count

################
# Type check
# Write a function named only_ints that takes two parameters. Your function should return True if both parameters are integers, and False otherwise.

# For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.

def only_ints(x, y):
    return type(x) == int and type(y) == int
        

################
# Double letters   
# The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row. 
# For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.

# Define a function named double_letters that takes a single parameter. The parameter is a string.
# Your function must return True if there are two identical letters in a row in the string, and False otherwise.

def double_letters(string):
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return True
    return False

################
# Adding and removing dots
# Write a function named add_dots that takes a string and adds "." in between each letter. 
# For example, calling add_dots("test") should return the string "t.e.s.t".

# Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. 
# For example, calling remove_dots("t.e.s.t") should return "test".

# If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.

# (You may assume that the input to add_dots does not itself contain any dots.

def add_dots(str):
    word = '.'.join(str)
    return word

def remove_dots(str):
    word = ''
    for char in str:
        if char == '.':
            continue
        else:
            word += char
    return word

################
# Counting syllables
# Define a function named count that takes a single parameter. 
# The parameter is a string. The string will contain a single word divided into syllables by hyphens, 
# such as these:

# "ho-tel"
# "cat"
# "met-a-phor"
# "ter-min-a-tor"
# Your function should count the number of syllables and return it.

# For example, the call count("ho-tel") should return 2.

def count(word):
    new = word.split('-')
    return len(new)

################
# Two strings are anagrams if you can make one from the other by rearranging the letters.

# Write a function named is_anagram that takes two strings as its parameters. 
# Your function should return True if the strings are anagrams, and False otherwise.

# For example, the call is_anagram("typhoon", "opython") should return True 
# while the call is_anagram("Alice", "Bob") should return False.

def is_anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False
    
################
# Divisible by 3
# Define a function named div_3 that returns True if its single integer parameter is divisible by 3 and False otherwise.

# For example, div_3(6) is True because 6/3 does not leave any remainder. However div_3(5) is False because 5/3 leaves 2 as a remainder.

def div_3(num):
    if num % 3 == 0:
        return True
    else:
        return False
    
###############
# Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

# For example, calling all_equal([1, 1, 1]) should return True.
def all_equal(list):
    n = []
    for i in list:
        n.append(i)
        if i != n[0]:
            return False
    return True
        
print(all_equal([1,1,1]))

###############
# Define a function named triple_and that takes three parameters and returns True only if they are all True and False otherwise.

def triple_and(a,b,c):
    if a and b and c == True:
        return True
    else:
        return False
    
###############

# Write a function that takes a list of lists and flattens it into a one-dimensional list.

# Name your function flatten. It should take a single parameter and return a list.

# For example, calling:

# flatten([[1, 2], [3, 4]])
# Should return the list:

# [1, 2, 3, 4]

def flatten(n):
    empty = []
    for i in n:
        empty.extend(i)
    return empty

##############

# Consecutive zeros
# The goal of this challenge is to analyze a binary string consisting of only zeros and ones. 
# Your code should find the biggest number of consecutive zeros in the string. For example, given the string:

# "1001101000110"
# The biggest number of consecutive zeros is 3.

# Define a function named consecutive_zeros that takes a single parameter, 
# which is the string of zeros and ones. Your function should return the number described above

def consecutive_zeros(n):
    count = 0
    store = []
    for char in n:
        if int(char) == 0:
            count += 1
        else:
            store.append(count)
            count = 0
    store.append(count)
    return max(store)
    
print(consecutive_zeros("10110010101010"))

##############
# Check if Palindrome
def palindrome(n):
    if n == n[::-1]:
        return True
    else:
        return False
    
##############
#custom Zip

# The built-in zip function "zips" two lists. Write your own implementation of this function.
# Define a function named zap. The function takes two parameters, a and b. These are lists.
# Your function should return a list of tuples. Each tuple should contain one item from the a list and one from b.
# You may assume a and b have equal lengths.
# If you don't get it, think of a zipper.
# For example:
# zap(
#     [0, 1, 2, 3],
#     [5, 6, 7, 8]
# )
# Should return:
# [(0, 5),
#  (1, 6),
#  (2, 7),
#  (3, 8)]

def zap(a, b):
    result = []
    for _ in range(len(a)):
        result.append((a[_],b[_]))
    return result


# Min-maxing
# Define a function named largest_difference that takes a list of numbers as its only parameter.

# Your function should compute and return the difference between the largest and smallest number in the list.

# For example, the call largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2.

# You may assume that no numbers are smaller or larger than -100 and 100
def largest_difference(numb):
    maxs = max(numb)
    mins = min(numb)
    return (maxs - mins)

##############
# Up and down
# Define a function named up_down that takes a single number as its parameter. 
# Your function return a tuple containing two numbers; the first should be one lower than the parameter,
#  and the second should be one higher.

# For example, calling up_down(5) should return (4, 6).
def up_down(number):
    return (number - 1, number + 1)

##############
# List xor
# Define a function named list_xor. Your function should take three parameters: n, list1 and list2.
# Your function must return whether n is exclusively in list1 or list2.
# In other words, if n is in both lists or in none of the lists, return False. If n is in only one of the lists, return True.
# For example:
# list_xor(1, [1, 2, 3], [4, 5, 6]) == True
# list_xor(1, [0, 2, 3], [1, 5, 6]) == True
# list_xor(1, [1, 2, 3], [1, 5, 6]) == False
# list_xor(1, [0, 0, 0], [4, 5, 6]) == False

def list_xor(n,list1,list2):
    if n in list1 and n in list2:
        return False
    elif n not in list1 and n not in list2:
        return False
    else:
        return True

# Counting parameters
# Define a function param_count that takes a variable number of parameters. 
# The function should return the number of arguments it was called with.

# For example, param_count() should return 0, while param_count(2, 3, 4) should return 3.
def param_count(*n):
    return len(n)
    

##############

# We have two monkeys, a and b, and the parameters a_smile 
# and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.


# monkey_trouble(True, True) → True
# monkey_trouble(False, False) → True
# monkey_trouble(True, False) → False
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False

##############
# Given two int values, return their sum. 
# Unless the two values are the same, then return double their sum.
def sum_double(a, b):
  if a == b:
    return (a + b) * 2
  else:
    return a + b
  
  def sum_double(a, b):
  # Store the sum in a local variable
  sum = a + b
  
  # Double it if a and b are the same
  if a == b:
    sum = sum * 2
  return sum


##############
# Give me the discount
# Create a function in Python that accepts two parameters. 
# The first should be the full price of an item as an integer. 
# The second should be the discount percentage as an integer.

# The function should return the price of the item after the discount has been applied. 
# For example, if the price is 100 and the discount is 20, the function should return 80.
def discount(n1,n2):
    return (n1 -(n1*(n2/100)))
    
print(int(discount(120,55)))
  






