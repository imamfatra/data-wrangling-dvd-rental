import pandas as pd
from utils.data_validations import *

# handle mismatch name column
def handle_mismatch_column(actual_table: dict, requirement_table: dict) -> dict:
    # country table
    country_table = actual_table["country"]
    country_table["country_id"] = range(1, len(country_table) + 1) 
    country_table = country_table[["country_id", "country", "last_update"]]
    actual_table["country"] = country_table

    # city table
    city_table = actual_table["city"]
    country_table = actual_table["country"]
    city_merge = city_table.merge(
        country_table,
        how="inner",
        on="country"
    )
    city_merge = city_merge[["city_id", "country_id", "city", "last_update"]]
    actual_table["city"] = city_merge

    check_columns(actual_table, requirement_table)
    return actual_table

def remove_missing_values(actual_table: dict) -> dict:
    clean_actual_table = {}

    for table_name, df in actual_table.items():
        df = df.dropna()
        clean_actual_table[table_name] = df
    
    check_missing_values(clean_actual_table)
    return clean_actual_table

# match data type
def adjust_data_type(actual_table: dict, requirement_table: dict) -> dict:
    data_clean = {}

    for table_name, df in actual_table.items():
        requirment_type = {}
        for requirment_column in requirement_table[table_name]:
            column = requirment_column["column_name"]
            type_data = requirment_column["data_type"]
            requirment_type[column] = type_data

        for column_name in df.columns:
            df[column_name] = df[column_name].astype(requirment_type[column_name])

        data_clean[table_name] = df
    
    check_data_type(data_clean, requirement_table)
    return data_clean

# remove duplicate data
def remove_duplicates(actual_table: dict) -> dict:
    data_clean = {}

    for table_name, df in actual_table.items():
        df = df.astype(str).drop_duplicates(keep="first")
        data_clean[table_name] = df

    check_duplicates_data(data_clean)
    return data_clean

# data cleaning all
def cleaning_all(actual_table: dict, requirement_table: dict) -> dict:
    actual_table = actual_table
    requirement_table = requirement_table

    table_clean = handle_mismatch_column(actual_table, requirement_table)
    table_clean = remove_missing_values(table_clean)
    table_clean = adjust_data_type(table_clean, requirement_table)
    table_clean = remove_duplicates(table_clean)

    return table_clean