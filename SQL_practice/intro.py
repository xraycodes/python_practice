import sqlite3

#connect to DB
con = sqlite3.connect('customer.db')

#creat a cursor 
c = con.cursor()

many_customers = [
                ('Wes', 'Brown', 'wes@brown.com'),
                ('Steph', 'King', 'steph@gmail.com'),
                ('Dan', 'Hook', 'dannhook@gmail.com'),
                ]

c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

print('command executed')

#Commit our command
con.commit()

#Close our connection(Good practice)
con.close()