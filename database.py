import sqlite3

connection = sqlite3.connect('db.db')

with open('memoria.sql') as f:
    connection.executescript(f.read())
    connection.commit()
    
connection.close()
