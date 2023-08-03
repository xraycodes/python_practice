import csv

input_filename = 'country_info.txt'

countries = {}
with open(input_filename, encoding='utf-8', newline='') as country_file:
    dict_reader = csv.DictReader(country_file, delimiter = '|')
    for row in dict_reader:
        # countries[country.casefold()] = country_dict
        countries[row['Country'].casefold()] = row
        # code_lookup[code.casefold()] = country
        countries[row['CC'].casefold()] = row

 
while True:
    chosen_country = input("What country would you like to know? ").casefold()
    if chosen_country in countries:
        country_data = countries[chosen_country]
        if country_data['Capital'] == '':
            print(f"{chosen_country} does not have a capital city")
        else:
            print(f"The capital of {chosen_country} is {country_data['Capital']}")
    elif chosen_country == 'quit':
        break
    else:
        print("Choose a country")
