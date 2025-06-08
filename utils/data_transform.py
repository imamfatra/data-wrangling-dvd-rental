import pandas as pd
from pandas import DataFrame

def generate_film_list_table(actual_table: dict) -> DataFrame:
    film_category_df = actual_table["film_category"]
    category_df = actual_table["category"]
    film_df = actual_table["film"]
    film_actor_df = actual_table["film_actor"]
    actor_df = actual_table["actor"]
    actor_df["full_name"] = actor_df["first_name"] + ' ' + actor_df["last_name"]

    film_list = category_df.merge(film_category_df, how="left", on="category_id", suffixes=("_x1", "_y1"))
    film_list = film_list.merge(film_df, how="left", on="film_id",suffixes=("_x2", "_y2"))
    film_list = film_list.merge(film_actor_df, how="inner", on="film_id", suffixes=("_x3", "_y3"))
    film_list = film_list.merge(actor_df, how="inner", on="actor_id", suffixes=("_x4", "_y4"))
    film_list = film_list.groupby(['film_id', 'title', 'description', 'name', 'rental_rate', 
                                   'length', 'rating'])['full_name'].apply(lambda x: ', '.join(x))
    film_list = pd.DataFrame(film_list)
    film_list = film_list.reset_index()

    rename_colom_map = {
        'film_id': 'fid',
        'name': 'category',
        'rental_rate': 'prince',
        'full_name': 'actors'
    }

    film_list.rename(columns=rename_colom_map, inplace=True)
    return film_list
