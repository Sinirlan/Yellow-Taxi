import pandas as pd

#Import Parquet file
raw_file = pd.read_parquet('yellow_tripdata_2020-01.parquet')

#Create new [dropoff_date] column
raw_file['dropoff_date'] = raw_file['tpep_dropoff_datetime'].dt.to_period('D')

#Group by newly created [dropoff_date] column and save to separate files
for (dropoff_date), group in raw_file.groupby(['dropoff_date']):
    group.to_parquet(f'{dropoff_date}.parquet')