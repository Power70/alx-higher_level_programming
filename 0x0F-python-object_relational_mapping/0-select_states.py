#!/usr/bin/python3
import MySQLdb
from sys import argv
"""
Access to the database and get the states from the databse
"""
    
db = MySQLdb.connect(host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

cur = db.cursor()
cur.execute("SELECT * FROM states")
rows = cur.fetchall()
for row in rows:
    print(row)