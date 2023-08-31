import sqlite3

#connect to DB
con = sqlite3.connect('customer.db')

#creat a cursor 
c = con.cursor()

#query the DB
c.execute("SELECT * FROM customers")
# c.fetchone()   FETCHES LAST ITEM
# c.fetchmany(3)  FETCHES 3 or desired parameter
print(c.fetchall())

print('command executed')

#Commit our command
con.commit()

#Close our connection(Good practice)
con.close()