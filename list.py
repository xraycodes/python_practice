#Removing outliers in a ORDERED data set

data = [4,5,104,105,110,120,130,140,180,201,250,350,360]

min_valid = 100
max_valid = 200

stop = 0

print(len(data))
print(data)
#process the low values in the list
for index,value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)
del data[:stop]
print(data)

#process the high values in the list 
start = 0

for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        start = index + 1
        break
print(start)
del data[start:]
print(data)