#!/usr/bin/python3
"""
Take in an argument and display all values in the states table
of hbtn_0e_0_usawhere name matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{}' ORDER BY id;"
                .format(sys.argv[4]))
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
