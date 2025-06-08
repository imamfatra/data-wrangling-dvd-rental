import pandas as pd
from pandas import DataFrame

def data_2() -> DataFrame:
    country_raw = "https://raw.githubusercontent.com/rahilpacmann/case-data-wrangling-api/main/country.csv"
    country_df = pd.read_csv(country_raw)
    
    return country_df