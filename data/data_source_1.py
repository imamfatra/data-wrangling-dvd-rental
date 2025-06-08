import pandas as pd
from pandas import DataFrame

def data_1() -> DataFrame:
    city_raw = "https://raw.githubusercontent.com/rahilpacmann/case-data-wrangling-api/main/city.csv"
    city_df = pd.read_csv(city_raw)
    
    return city_df