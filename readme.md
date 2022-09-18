# Yellow Taxi sample files


## Dependecies
- pandas  (https://pandas.pydata.org/)
- pyarrow (https://arrow.apache.org/docs/python/index.html)
- mysql-connector (https://dev.mysql.com/doc/connector-python/en/)
- sqlalchemy (https://www.sqlalchemy.org/)


## beyond-splitter

This script will split one big parquet file into smaller ones each covering one day worth of data.

Usage:

    python beyond-splitter.py <source> <destination>

Example:

    python beyond-splitter.py C:\Yellow-Taxi\yellow_tripdata_2020-01.parquet C:\Yellow-Taxi\output

If destination folder does not exist it will be created.


## beyond-loader
This script loads parquet files contained in provided folder and loads them to MySQL database

Usage:

    python beyond-loader.py <source folder>
Example:

    python beyond-loader.py C:\Yellow-Taxi\output
