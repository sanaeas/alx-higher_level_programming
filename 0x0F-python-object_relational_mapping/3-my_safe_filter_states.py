#!/usr/bin/python3
"""
Take in an argument and display all values in the states table
of hbtn_0e_0_usa where name matches the argument
that is safe from MySQL injections
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    state_name = argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s;", (state_name, ))
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
