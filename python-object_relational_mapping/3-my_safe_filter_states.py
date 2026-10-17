#!/usr/bin/python3
"""Safely list states matching a name supplied by the user."""

import MySQLdb
import sys


def main():
    """Connect to MySQL and retrieve states using a safe parameter."""
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
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (sys.argv[4],)
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
