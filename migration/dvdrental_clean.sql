-- Membuat skema public jika belum ada
CREATE SCHEMA IF NOT EXISTS public;

-- Buat tabel
CREATE TABLE IF NOT EXISTS public.actor (
    actor_id SERIAL PRIMARY KEY,
    last_update TIMESTAMP,
    first_name VARCHAR,
    last_name VARCHAR
);

CREATE TABLE IF NOT EXISTS public.store (
    store_id SERIAL PRIMARY KEY,
    manager_staff_id INTEGER,
    address_id INTEGER,
    last_update TIMESTAMP
);

CREATE TABLE IF NOT EXISTS public.address (
    last_update TIMESTAMP,
    city_id INTEGER,
    address_id SERIAL PRIMARY KEY,
    district VARCHAR,
    phone VARCHAR,
    postal_code VARCHAR,
    address VARCHAR,
    address2 VARCHAR
);

CREATE TABLE IF NOT EXISTS public.category (
    category_id SERIAL PRIMARY KEY,
    last_update TIMESTAMP,
    name VARCHAR
);

CREATE TABLE IF NOT EXISTS public.city (
    city_id SERIAL PRIMARY KEY,
    country_id INTEGER,
    last_update TIMESTAMP,
    city VARCHAR
);

CREATE TABLE IF NOT EXISTS public.country (
    country_id SERIAL PRIMARY KEY,
    last_update TIMESTAMP,
    country VARCHAR
);

CREATE TABLE IF NOT EXISTS public.customer (
    active INTEGER,
    store_id INTEGER,
    create_date TIMESTAMP,
    last_update TIMESTAMP,
    customer_id SERIAL PRIMARY KEY,
    address_id INTEGER,
    activebool BOOLEAN,
    first_name VARCHAR,
    last_name VARCHAR,
    email VARCHAR
);

CREATE TABLE IF NOT EXISTS public.film_actor (
    actor_id SERIAL PRIMARY KEY,
    film_id INTEGER,
    last_update TIMESTAMP
);
 
CREATE TABLE IF NOT EXISTS public.film_category (
    film_id SERIAL PRIMARY KEY,
    category_id INTEGER,
    last_update TIMESTAMP
);

CREATE TABLE IF NOT EXISTS public.inventory (
    inventory_id SERIAL PRIMARY KEY,
    film_id INTEGER,
    store_id INTEGER,
    last_update TIMESTAMP
);

CREATE TABLE IF NOT EXISTS public.language (
    language_id SERIAL PRIMARY KEY,
    last_update TIMESTAMP,
    name VARCHAR
);

CREATE TABLE IF NOT EXISTS public.rental (
    rental_id SERIAL PRIMARY KEY,
    rental_date TIMESTAMP,
    inventory_id INTEGER,
    customer_id INTEGER,
    return_date TIMESTAMP,
    staff_id INTEGER,
    last_update TIMESTAMP
);

CREATE TABLE IF NOT EXISTS public.staff (
    picture VARCHAR,
    address_id INTEGER,
    store_id INTEGER,
    active BOOLEAN,
    last_update TIMESTAMP,
    staff_id SERIAL PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    password VARCHAR,
    email VARCHAR,
    username VARCHAR
);

CREATE TABLE IF NOT EXISTS public.payment (
    payment_id SERIAL PRIMARY KEY,
    customer_id INTEGER,
    staff_id INTEGER,
    rental_id INTEGER,
    amount FLOAT,
    payment_date TIMESTAMP
);

CREATE TABLE IF NOT EXISTS public.film (
    fulltext VARCHAR,
    rating VARCHAR,
    last_update TIMESTAMP,
    film_id SERIAL PRIMARY KEY,
    release_year INTEGER,
    language_id INTEGER,
    rental_duration INTEGER,
    rental_rate FLOAT,
    length INTEGER,
    replacement_cost FLOAT,
    title VARCHAR,
    description VARCHAR,
    special_features VARCHAR
);