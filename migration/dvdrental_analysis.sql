-- Membuat skema public jika belum ada
CREATE SCHEMA IF NOT EXISTS public;

-- Membuat tabel film_list
CREATE TABLE IF NOT EXISTS public.film_list (
    fid SERIAL PRIMARY KEY,
    title VARCHAR,
    description VARCHAR,
    category VARCHAR,
    price FLOAT,
    length INTEGER,
    rating VARCHAR,
    actors VARCHAR
);