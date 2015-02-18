#! /usr/bin/python3

import sqlite3

conn = sqlite3.connect('db.sqlite3')
print("Opened database successfully")

try:
    conn.execute(
        "CREATE TABLE COMPANY \
        (ID INT PRIMARY KEY NOT NULL,\
        NAME TEXT NOT NULL,\
        AGE INT NOT NULL,\
        ADDRESS CHAR(50),\
        SALARY REAL); "
    )
except Exception as e:
    print(str(e))
else:
    print("Table created successfully")

conn.close()
