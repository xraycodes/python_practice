import sqlite3

#connect to DB
con = sqlite3.connect('customer.db')

#creat a cursor 
c = con.cursor()

#creata a table
c.execute("""CREATE TABLE customers (
    first_name text, 
    last_name text,
    email text
)""" )

#Commit our command
con.commit()

#Close our connection(Good practice)
con.close()