import sqlite3

#connect to DB
con = sqlite3.connect('customer.db')

#creat a cursor 
c = con.cursor()

#Drop the table
c.execute("DROP TABLE customers")

#Commit our command
con.commit()

c.execute("SELECT * FROM customers")
items = c.fetchall()
print(items)

#Close our connection(Good practice)
con.close()