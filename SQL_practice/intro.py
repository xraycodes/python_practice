import sqlite3

#connect to DB
con = sqlite3.connect('customer.db')

#creat a cursor 
c = con.cursor()

#Query the DB - ORDER BY
c.execute("SELECT rowid, * FROM customers LIMIT 2 ")
items = c.fetchall()
for item in items:
    print(item)

#Commit our command
con.commit()

#Close our connection(Good practice)
con.close()