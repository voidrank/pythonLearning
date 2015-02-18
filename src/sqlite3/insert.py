import sqlite3

conn = sqlite3.connect('db.sqlite3')
conn.execute(
    "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    VALUES (1, 'Paul', 32, 'California', 20000.0) "
)

conn.execute(
    "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    VALUES (2, 'voidrank', 99999, 'TTT', 20000.0)"
)

conn.commit()
print ("Record created successfully")
conn.close()
