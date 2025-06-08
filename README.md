# Data Wrangling : DVD Rental ETL

## 1. Preparation

- **Install docker**
- **Menyiapkan data source**
  - Masuk ke folder `data-source`
  - Jalankan perintah
    ```bash
    docker compose up -d
    ```
- **Menyiapkan data warehouse**
  - Masuk ke folder `data-warehouse`
  - Jalankan perintah
    ```bash
    docker compose up -d
    ```
  - Keluar dari folder `data-warehouse` dan masuk ke folder `migration`
  - Jalankan perintah
    ```bash
    python -m migration.migration_table_dwh
    ```

## 2. Usage

- Melakukan validasi:
  ```bash
  python -m utils.data_validations
  ```
- Menjalankan main (ekstrak -> transform -> load):
  ```bash
  python main.py
  ```
