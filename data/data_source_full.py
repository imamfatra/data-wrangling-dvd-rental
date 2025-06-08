from data.data_source_1 import data_1
from data.data_source_2 import data_2
from data.data_source_3 import get_table_data
from pandas import DataFrame


def data_full() -> dict[str, DataFrame]:
    # Dari data source 1
    city_df = data_1()

    # Dari data source 2
    country_df = data_2()

    # Dari data source 3
    actor_df = get_table_data('actor')
    store_df = get_table_data('store')
    address_df = get_table_data('address')
    category_df = get_table_data('category')
    customer_df = get_table_data('customer')
    film_actor_df = get_table_data('film_actor')
    film_category_df = get_table_data('film_category')
    inventory_df = get_table_data('inventory')
    language_df = get_table_data('language')
    rental_df = get_table_data('rental')
    staff_df = get_table_data('staff')
    payment_df = get_table_data('payment')
    film_df = get_table_data('film')

    data_dict = {
        "actor": actor_df,
        "store": store_df,
        "address": address_df,
        "category": category_df,
        "customer": customer_df,
        "film_actor": film_actor_df,
        "film_category": film_category_df,
        "inventory": inventory_df,
        "language": language_df,
        "rental": rental_df,
        "staff": staff_df,
        "payment": payment_df,
        "film": film_df,
        "city": city_df,
        "country": country_df    
    }

    return data_dict