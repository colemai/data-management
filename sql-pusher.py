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
	Take the master csv from a specified path
	Return it
	"""
	with open(csv_path) as csver:
		df = pd.read_csv(csver)
	return df

def insert_data(data):
	"""
	Input: List with all data you want to upload to a specific column file
	Effect: Pushes given data to specified table 
	"""
	query = "INSERT INTO Species(nameLatin) " \
			"VALUES(%s)"
 
	try:
		mysql_conn = MySQLdb.connect(host=argv[2], user=argv[3], 
								 passwd=argv[4], db=argv[5])
		cursor = mysql_conn.cursor()
		cursor.executemany(query, data)
 
		mysql_conn.commit()
	except Error as e:
		print('Error:', e)
 
	finally:
		cursor.close()
		mysql_conn.close()
 
def main(df):
	data = df['Soort']
	data = data.dropna().tolist()
	insert_data(data)

if __name__ == "__main__":
	print('commence')
	df = intake_master_csv(argv[1])
	main(df)