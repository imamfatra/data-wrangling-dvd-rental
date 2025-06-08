import pandas as pd
from pandas import DataFrame
from utils.data_warehouse_connection import source_postgres_engine

def get_table_data(table_name: str) -> DataFrame:
    try: 
        db_name = "dvdrental"
        engine = source_postgres_engine(db_name)

        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql(query, engine)
        return df
    except Exception as err:
        print("Error: ", err)
        return pd.DataFrame()