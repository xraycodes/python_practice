import sqlite3

#connect to DB
con = sqlite3.connect('customer.db')

#creat a cursor 
c = con.cursor()

#query the DB
c.execute("SELECT * FROM customers WHERE last_name LIKE 'Br%'")
# c.fetchone()   FETCHES FIRST ITEM
# c.fetchmany(3)  FETCHES first 3 or desired parameter
# print(c.fetchall())
# print(c.fetchone())
v = c.fetchall()
for items in v:
   print(items)
print('command executed')

#Commit our command
con.commit()

#Close our connection(Good practice)
con.close()