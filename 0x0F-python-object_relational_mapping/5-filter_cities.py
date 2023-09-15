#!/usr/bin/python3
"""
List all cities of a given state
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    state_name = argv[4]
    cur.execute("SELECT cities.name \
                FROM cities JOIN states ON cities.state_id = states.id \
                WHERE states.name = %s;", (state_name, ))
    cities = cur.fetchall()
    cities_list = []
    for city in cities:
        cities_list.append(city[0])
    print(', '.join(cities_list))

    cur.close()
    db.close()
