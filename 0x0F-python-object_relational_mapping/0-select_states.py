#!/usr/bin/python3
"""
This module lists all states from the database `hbtn_0e_0_usa`.

Usage:
    Execute this script with MySQL username, password, and database name
    as arguments. The script connects to the MySQL database and prints
    all states sorted in ascending order by their ids.

    Example:
        $ ./<script_name>.py mysql_username mysql_password database_name
"""

import MySQLdb
from sys import argv

def fetch_states(username, password, database):
    """
    Fetches and prints all states from a given database.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the database to query.

    Returns:
        None
    """
    db = MySQLdb.connect(host="localhost", user=username, port=3306, passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == '__main__':
    if len(argv) == 4:
        fetch_states(argv[1], argv[2], argv[3])
    else:
        print("Usage: ./<script_name>.py <mysql_username> <mysql_password> <database_name>")
