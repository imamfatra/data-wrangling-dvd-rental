from data import data_source_full
from data import requirments
from utils import data_cleaning
from utils import data_warehouse_connection
from utils import data_transform
from pandas import DataFrame

import warnings
warnings.filterwarnings('ignore')

# load data to 'dvdrental_clean'
def load_dvdrental_clean(data: dict):
    engine = data_warehouse_connection.dw_postgres_engine("dvdrental_clean")

    for table_name, df in data.items():
        df.to_sql(table_name, engine, if_exists='replace', index=False)

    engine.dispose()

# load data to 'dvdrental_analysis'
def load_dvdrental_analysis(data: DataFrame):
    engine = data_warehouse_connection.dw_postgres_engine("dvdrental_analysis")

    data.to_sql("film_list", engine, if_exists='replace', index=False)
    engine.dispose()

def main():
    actual_data = data_source_full.data_full()
    requirement_data = requirments.requirements_data()

    data_clean = data_cleaning.cleaning_all(
        actual_data, requirement_data
    )

    load_dvdrental_clean(data_clean)
    print("Load data to dvdrental_clean successfully")

    # load_dvdrental_analysis(data_clean)
    film_list = data_transform.generate_film_list_table(actual_data)
    load_dvdrental_analysis(film_list)
    print("Load data to dvdrental_analysis successfully")

if __name__ == "__main__":
    main()
