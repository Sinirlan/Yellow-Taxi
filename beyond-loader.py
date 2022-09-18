import os
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import argparse

#Prepare command line arguements
parser = argparse.ArgumentParser(description="Simple Parquet file loader",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('src', help='Source folder location')
args = vars(parser.parse_args())
source = args['src']

# define DB connection
engine = create_engine('mysql+mysqlconnector://NYC_user:Pr377y-5eCur3_pa55w0rd@192.168.1.12:3306/yellow_cabs', echo=False)
# storing credentials in open text is bad idea, did it to keep things simple.



# #truncate staging - uncomment if you want to clear table before each batch 
#engine.execute("TRUNCATE TABLE yellow_cabs.trips")

#check if source folder exists 
if not os.path.exists(source):
    raise Exception("Provided folder: " + source + " does not exist")

source = source + '/'

for fileName in os.listdir(source):
    if fileName.endswith('.parquet'):
        print('Processing: ' +fileName) #little feedback to console to let know user that program is doing something
        raw_file = pd.read_parquet(source + fileName)
        raw_file = raw_file.drop(['dropoff_date'],axis=1) #correcting mistake from beyond-splitter.py, it made it easier to split files by day but introduced _mysql_connector.MySQLInterfaceError: Python type Period cannot be converted
        raw_file.to_sql(name='trips', con=engine, if_exists = 'append', index=False)