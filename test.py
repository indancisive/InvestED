import sqlite3

conn = sqlite3.connect("db.sqlite3")
cursor = conn.execute("SELECT * FROM investmate_backend_stock")
rows = cursor.fetchall()
print(rows[0])