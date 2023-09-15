#!/usr/bin/python3
"""
Take in an argument and display all values in the states table
of hbtn_0e_0_usawhere name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{}' ORDER BY id;"
                .format(argv[4]))
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
