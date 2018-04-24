#!/usr/bin/env python3
"""
Author: Ian Coleman
Example call: python csv-parser.py csv_folder
Input: path to folder with all csv files
Output: Other CSV Files

"""

from sys import argv
import pdb
import csv
import pandas as pd
import os
import glob


def intake_csv_files(csv_path):
	"""
	Input: Seed csv in the original format 
	Output: Whichever columns we want
	"""
	aggregate_df = pd.DataFrame()
	for csv_file in glob.iglob('csv-files/*.csv'):
		with open(csv_file) as csver:
			df = pd.read_csv(csver, usecols=['Soort', 'Voorraad','Prijs', 'Niet inpakken'])
			aggregate_df = df.join(aggregate_df)
	return aggregate_df


def output_data_with_pandas(input_df):
	"""
	Input: A dataframe to be turned into a new csv
	Output: Creates a csv in the current folder of this df
	"""
	# Create Species CSV
	output_df = pd.DataFrame(columns=['speciesID','nameDutch','nameLatin','nameEnglish','package','expirationTime','pricePerBag', 'seedsPerBag'])
	output_df['nameLatin'] = input_df['Soort']
	output_df['pricePerBag'] = input_df['Prijs']
	output_df.to_csv('output-csvs/species.csv', index=False)
	input_df.to_csv('master.csv', index=False)

if __name__ == "__main__":
	df2 = intake_csv_files(argv[1])
	trimmed_df = output_data_with_pandas(df2)
	
