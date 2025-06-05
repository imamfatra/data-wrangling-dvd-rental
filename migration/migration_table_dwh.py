from sqlalchemy import text
from utils.data_warehouse_connection import dw_postgres_engine

def migration_table(database_name:str, file_path: str):
    # create table in the database
    engine = dw_postgres_engine(database_name)

    with open(file_path, "r") as f:
        sql = f.read()

    with engine.connect() as conn:
        conn.execute(text(sql))
        conn.commit()
    

def main():
    # migrasi tabel ke database dvdrental_clean
    migration_table(
        "dvdrental_clean",
        "./migration/dvdrental_clean.sql"
    )
    print("migrasi tabel ke database dvdrental_clean berhasil")

    # migrasi tabel ke database dvdrental_analysis
    migration_table(
        "dvdrental_analysis",
        "./migration/dvdrental_analysis.sql"
    )
    print("migrasi tabel ke database dvdrental_analysis berhasil")

if __name__ == "__main__":
    main()