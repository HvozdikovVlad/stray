#import sqlite3
#
#connection = sqlite3.connect("itstep_DB.sl3", 5)
#cur = connection.cursor()
#print(connection)
#print(cur)
#connection.close()

import sqlite3

connection = sqlite3.connect("itstep_DB.sl3", 5)
cur = connection.cursor()
cur.execute("INSERT INTO first_table (name) VALUES ('Ann');")
cur.execute("INSERT INTO first_table (name) VALUES ('Kats');")
cur.execute("INSERT INTO first_table (name) VALUES ('John');")
connection.commit()
cur.execute("SELECT rowid, name FROM first_table;")
connection.commit()
res = cur.fetchall()
print(res)
connection.close()