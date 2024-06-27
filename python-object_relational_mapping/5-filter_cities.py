#!/usr/bin/python3
"""
This script connects to a MySQL database
"""

import sys
import MySQLdb as mysql

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    st_name = sys.argv[4]

    db = mysql.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = db.cursor()
    cursor.execute("""
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE BINARY states.name = %s AND states.name IS NOT NULL
    ORDER BY cities.id ASC;""".format(st_name), (st_name, ))
    result = cursor.fetchall()

    for x in result:
        print(x[0], end=", " if x != result[-1] else "")
    print()

    cursor.close()
    db.close()
