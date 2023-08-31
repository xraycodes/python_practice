import sqlite3

#connect to DB
con = sqlite3.connect('customer.db')

#creat a cursor 
c = con.cursor()

c.execute("INSERT INTO customers VALUES ('John', 'Elder', 'john@gmail.com')")

print('command executed')

#Commit our command
con.commit()

#Close our connection(Good practice)
con.close()