#!/usr/bin/python3
"""
This script connects to a MySQL database and selects all the rows from the 'states' table.
"""

import sys
import MySQLdb as mysql

"""main function and stuff"""
def main():
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = mysql.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    result = cursor.fetchall()

    for x in result:
        print(x)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()