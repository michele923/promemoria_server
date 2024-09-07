import sqlite3

connection = sqlite3.connect('files/db.sqlite')

with open('files/db_init.sql') as f:
    connection.executescript(f.read())
    connection.commit()

connection.close()
