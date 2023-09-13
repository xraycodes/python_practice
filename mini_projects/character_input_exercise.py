#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old. 

YEAR = 2023

user_name = input("What is your name? ")
user_age = int(input("What is your age? "))

age_100_year = (100 - user_age) + YEAR

print(f"{user_name} is currently {user_age} and will be 100 in year {age_100_year}")


