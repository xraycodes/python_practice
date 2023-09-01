import sqlite3

#connect to DB
con = sqlite3.connect('customer.db')

#creat a cursor 
c = con.cursor()

#delete record
c.execute("DELETE from customers WHERE rowid = 5")

#Query the DB
c.execute("SELECT rowid, * FROM customers")
items = c.fetchall()
for item in items:
    print(item)

#Commit our command
con.commit()

#Close our connection(Good practice)
con.close()