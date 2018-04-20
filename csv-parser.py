#!/usr/bin/env python3
"""
Author: Ian Coleman
Input: CSV Files
Output: Other CSV Files

"""

from sys import argv
import pdb
import csv
import pandas as pd



def intake_data(file_path):
	"""
	Input: a folder of csv files used by the customer
	Output: a folder of csv files in the format of our sql db
	"""
	with open(file_path) as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in spamreader:
			print (', '.join(row))

# def intake_data_with_pandas(file_path):
# 	"""
# 	"""
# 	with open(file_path) as csvfile:
# 		df = pd.read_csv(csvfile)
# 		# name_column = df['name']
# 		# return(name_column)
# 		df2 = df[['name', 'age']].copy()
# 		return df2

def intake_seed_db(seed_csv_path):
	"""
	Input: Seed csv in the original format 
	Output: Whichever columns we want
	"""
	with open(seed_csv_path) as csvfile:
		df = pd.read_csv(csvfile, usecols=['Soort', 'Voorraad','Prijs', 'Niet inpakken'])
		trimmed_df = df.iloc[:,0:4]
		return trimmed_df


def output_data_with_pandas(input_df):
	"""
	Input: A dataframe to be turned into a new csv
	Output: Creates a csv in the current folder of this df
	"""
	output_df = pd.DataFrame(columns=['speciesID','nameDutch','nameLatin','nameEnglish','package','expirationTime','pricePerBag', 'seedsPerBag'])
	output_df['nameLatin'] = input_df['Soort']
	output_df['pricePerBag'] = input_df['Prijs']
	output_df.to_csv('outputter.csv', index=False)




if __name__ == "__main__":
	df2 = intake_seed_db(argv[1])
	trimmed_df = output_data_with_pandas(df2)
	
