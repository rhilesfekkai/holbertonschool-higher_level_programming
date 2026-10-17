#!/usr/bin/python3
"""List cities belonging to a state specified by the user."""

import MySQLdb
import sys


def main():
    """Connect to MySQL and display cities belonging to a given state."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cur = db.cursor()
    cur.execute(
        "SELECT cities.name FROM cities "
        "INNER JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s ORDER BY cities.id ASC",
        (sys.argv[4],)
    )
    cities = cur.fetchall()
    if cities:
        print(", ".join(city[0] for city in cities))

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
