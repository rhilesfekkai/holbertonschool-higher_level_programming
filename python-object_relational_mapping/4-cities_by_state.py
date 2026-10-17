#!/usr/bin/python3
"""List all cities with their corresponding states."""

import MySQLdb
import sys


def main():
    """Connect to MySQL and display cities with their state names."""
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
        "SELECT cities.id, cities.name, states.name "
        "FROM cities JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
