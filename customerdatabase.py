def add_cust_values(customername, customeradr):
    import sqlite3 as sq
    conn = sq.connect("db\customers.db")
    
    c = conn.cursor()

    c.execute("INSERT INTO customers VALUES (?,?)", (str(customername), str(customeradr)))
    conn.commit()
    conn.close()
    
    
    
def get_cust_values(customerdata):
    import sqlite3 as sq
    conn = sq.connect("db\customers.db")
    
    c = conn.cursor()
#    c.execute("""CREATE TABLE customers (
#        cust text,
#        custadr integer
#        )""")
    cust_query = "Select * from customers"
    c.execute(cust_query)

    result = c.fetchall()
    for row in result:
        customerdata.append(row[0] + ": " + str(row[1]))
     
    conn.close()
    return customerdata

def delete_cust_values():
    import sqlite3 as sq
    conn = sq.connect("db\customers.db")
    c = conn.cursor()
    c.execute("DELETE FROM customers")
    conn.commit()
    conn.close()
    