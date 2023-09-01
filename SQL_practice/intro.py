import sqlite3
# #connect to DB
# con = sqlite3.connect('customer.db')
# #creat a cursor 
# c = con.cursor()

# customers = [('Bob', 'Elder', 'bobelder@gmail.com'),('Jim', 'Bob', 'jimbob24@gmail.com'),('Kim','Slice', 'kimboslice@gmail.com')]
# c.executemany("INSERT INTO customers VALUES (?,?,?)", customers)

# con.commit()

#query the DB and return all records
def show_all():
    #connect to DB
    con = sqlite3.connect('customer.db')
    #creat a cursor 
    c = con.cursor()

    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()
    for item in items:
        print(item)
        
    #Commit our command
    con.commit()
    #Close our connection(Good practice)
    con.close()

def add_one(first, last, email):
    #Add new record to table
    #connect to DB
    con = sqlite3.connect('customer.db')
    #creat a cursor 
    c = con.cursor()
    c.execute("INSERT INTO customers VALUES(?,?,?)", (first, last, email))
    #Commit our command
    con.commit()
    #Close our connection(Good practice)
    con.close()

def many_entry(entries):
    con = sqlite3.connect('customer.db')
    #creat a cursor 
    c = con.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", entries)
    #Commit our command
    con.commit()
    #Close our connection(Good practice)
    con.close()

def delete_one(id):
    #delete entry
    con = sqlite3.connect('customer.db')
    #creat a cursor 
    c = con.cursor()
    c.execute(f"DELETE from customers WHERE rowid = {id}")
     #Commit our command
    con.commit()
    #Close our connection(Good practice)
    con.close()

def where_query(info):
    #delete entry
    con = sqlite3.connect('customer.db')
    #creat a cursor 
    c = con.cursor()
    c.execute(f"SELECT rowid, * FROM customers WHERE first_name LIKE '%{info}'")
    items = c.fetchall()
    for item in items:
        print(item)
    #Commit our command
    con.commit()
    #Close our connection(Good practice)
    con.close()


