def add_org_values(orgname, orgnr):
    import sqlite3 as sq
    conn = sq.connect("db\org.db")
    
    c = conn.cursor()

    c.execute("INSERT INTO orgs VALUES (?,?)", (str(orgname), str(orgnr)))
    conn.commit()
    conn.close()
    
    
    
def get_org_values(orgdata):
    import sqlite3 as sq
    conn = sq.connect("db\org.db")
    
    c = conn.cursor()
    org_query = "Select * from orgs"
    c.execute(org_query)
    #c.execute("""CREATE TABLE orgs (
    #        org text,
    #        orgnr integer
    #        )""")
    result = c.fetchall()
    for row in result:
        orgdata.append(row[0] + ": " + str(row[1]))
    conn.close()
    return orgdata

def delete_org_values():
    import sqlite3 as sq
    conn = sq.connect("db\org.db")
    c = conn.cursor()
    c.execute("DELETE FROM orgs")
    conn.commit()
    conn.close()