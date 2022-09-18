import os
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description="Simple Parquet splitter",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('src', help='Source file location')
parser.add_argument('dest', help='Destination folder for split files')
args = vars(parser.parse_args())

source = args['src']
destination = args['dest']

#Import Parquet file
raw_file = pd.read_parquet(source)

#Create new [dropoff_date] column
raw_file['dropoff_date'] = raw_file['tpep_dropoff_datetime'].dt.to_period('D')

if not os.path.exists(destination):
    os.mkdir(destination)


#Group by newly created [dropoff_date] column and save to separate files
for (dropoff_date), group in raw_file.groupby(['dropoff_date']):
    group.to_parquet(destination + f'/{dropoff_date}.parquet')