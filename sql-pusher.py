#!/usr/bin/env python
"""
Author: Internet
Call: python sql-pusher.py csv host user pw db
Input: 
Output:
Effect:  

"""

import csv
import MySQLdb
from sys import argv
from mysql.connector import MySQLConnection, Error
import pdb
import pandas as pd
# from python_mysql_dbconfig import read_db_config

def intake_master_csv(csv_path):
	"""
	"""
	with open(csv_path) as csver:
		df = pd.read_csv(csver)
	return df

def insert_data(books):
	query = "INSERT INTO Species(nameLatin) " \
			"VALUES(%s)"
 
	try:
		mysql_conn = MySQLdb.connect(host=argv[2], user=argv[3], 
								 passwd=argv[4], db=argv[5])
		cursor = mysql_conn.cursor()
		cursor.executemany(query, books)
 
		mysql_conn.commit()
	except Error as e:
		print('Error:', e)
 
	finally:
		cursor.close()
		mysql_conn.close()
 
def main(df):
	data = df['Soort']
	data = data.dropna().tolist()
	# pdb.set_trace()
	insert_data(data)

if __name__ == "__main__":
	print('commence')
	df = intake_master_csv(argv[1])
	main(df)

	# mysql_conn = MySQLdb.connect(host=argv[2], user=argv[3], 
	# 							 passwd=argv[4], db=argv[5])
	# mysql_cursor = mysql_conn.cursor()

	# f = open(argv[1])
	# csv_f = csv.reader(f)

	# for row in csv_f:
	# 	mysql_cursor.execute("""INSERT INTO Species (col1, col2, col3) VALUES(%s, %s, %s)""",
	# 						 (row[0], row[1], row[2]))

	# mysql_conn.commit()
	# mysql_cursor.close()