import csv

input_filename = 'country_info.txt'

dialect = csv.excel
dialect.delimiter = '|'

countries = {}
with open(input_filename, encoding='utf-8', newline='') as country_file:
    # Get the column headings from the first line of file
    headings = country_file.readline().strip('\n').split(dialect.delimiter)
    for index, heading in enumerate(headings):
        headings[index] = heading.casefold()

    dict_reader = csv.DictReader(country_file, dialect=dialect, fieldnames=headings)
    for row in dict_reader:
        # countries[country.casefold()] = country_dict
        countries[row['country'].casefold()] = row
        # code_lookup[code.casefold()] = country
        countries[row['cc'].casefold()] = row
        
while True:
    chosen_country = input("What country would you like to know? ").casefold()
    if chosen_country in countries:
        country_data = countries[chosen_country]
        if country_data['capital'] == '':
            print(f"{chosen_country} does not have a capital city")
        else:
            print(f"The capital of {chosen_country} is {country_data['capital']}")
    elif chosen_country == 'quit':
        break
    else:
        print("Choose a country")
