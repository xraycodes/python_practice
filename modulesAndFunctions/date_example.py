import datetime
import locale

locale.setlocale(locale.LC_ALL, '')  #checking locale of the computer to make sure the date displays in the locale langauge.

start = datetime.date(2022, 2, 4)
print(start)

pretty_start = start.strftime('%A %d %B, %Y')   #Check STRFTIME documentation for these % meanings
print(pretty_start)

year = start.year
month = start.month
day = start.day

print(f"{year} winter olmypics started on the day of {day} of month {month}")
 
today = datetime.date.today()  #prints out current date
print(today)
print(today.strftime('%A'))

print(today.weekday())