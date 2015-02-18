import sqlite3

conn = sqlite3.connect('db.sqlite3')
conn.execute("DELETE from COMPANY where ID=1")
conn.commit()

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3])

print("Operation done successfully")
conn.close()
