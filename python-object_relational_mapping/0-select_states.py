#!/usr/bin/python3
"""List all states from a MySQL database in ascending ID order."""

import MySQLdb
import sys


def main():
    """Connect to MySQL and display all states ordered by their IDs."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
