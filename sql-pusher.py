#!/usr/bin/env python
"""
Author: Internet
Call: python3 sql-pusher.py csv host user pw db
Input: 
Output:
Effect:  

"""

import csv
import MySQLdb
from sys import argv

mysql_conn = MySQLdb.connect(host=argv[2], user=argv[3], 
                             passwd=argv[4], db=argv[5])
mysql_cursor = mysql_conn.cursor()

f = open(argv[1])
csv_f = csv.reader(f)

for row in csv_f:
    mysql_cursor.execute("""INSERT INTO Iano (col1, col2, col3) VALUES(%s, %s, %s)""",
                         (row[0], row[1], row[2]))

mysql_conn.commit()
mysql_cursor.close()