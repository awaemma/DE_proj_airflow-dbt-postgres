
-- Create schema named "RAW" to hold all of the tables
CREATE SCHEMA IF NOT EXISTS RAW;
-- numeric(10, 2) not null,

-- DDL for customers table mapping to the olist_customers_dataset.csv
create table if not exists RAW.CUSTOMERS
(
    customer_id  uuid primary key,
    customer_unique_id uuid not null,
    customer_zip_code_prefix varchar,
    customer_city varchar,
    customer_state varchar


);

-- copy command to copy customers data
COPY RAW.CUSTOMERS (customer_id, customer_unique_id, customer_zip_code_prefix,customer_city,customer_state)
FROM '/data/olist_customers_dataset.csv' DELIMITER ',' CSV HEADER;

-- DDL for geolocation table mapping to the olist_geolocation_dataset.csv
create table if not exists RAW.GEOLOCATION
(
    geolocation_zip_code_prefix  varchar not null,
    geolocation_lat varchar not null,
    geolocation_lng varchar not null,
    geolocation_city varchar,
    geolocation_state varchar

);

-- copy command to copy geolocation data
COPY RAW.GEOLOCATION (geolocation_zip_code_prefix, geolocation_lat, geolocation_lng,geolocation_city,geolocation_state)
FROM '/data/olist_geolocation_dataset.csv' DELIMITER ',' CSV HEADER;


-- DDL for order_items table mapping to the olist_order_items_dataset.csv
create table if not exists RAW.ORDER_ITEMS
(
    order_id uuid not null,
    order_item_id  int not null,
    product_id  uuid not null,
    seller_id  uuid not null,
    shipping_limit_date timestamp,
    price numeric(10, 2) not null,
    freight_value  numeric(10, 2) not null
);


-- copy command to copy order_items data
COPY RAW.ORDER_ITEMS (order_id, order_item_id, product_id,seller_id,shipping_limit_date,price,freight_value)
FROM '/data/olist_order_items_dataset.csv' DELIMITER ',' CSV HEADER;

-- DDL for order_payment table mapping to the olist_order_payments_dataset.csv
create table if not exists RAW.ORDER_PAYMENTS
(
    order_id uuid not null,
    payment_sequential int not null,
    payment_type varchar,
    payment_installments int,
    payment_value numeric(10, 2) not null
);


-- copy command to copy order_payments data
COPY RAW.ORDER_PAYMENTS (order_id, payment_sequential, payment_type,payment_installments,payment_value)
FROM '/data/olist_order_payments_dataset.csv' DELIMITER ',' CSV HEADER;

-- DDL for order_review table mapping to the olist_order_reviews_dataset.csv
create table if not exists RAW.ORDER_REVIEWS
(
    review_id uuid not null,
    order_id uuid not null,
    review_score int,
    review_comment_title text,
    review_comment_message text,
    review_creation_date timestamp,
    review_answer_timestamp timestamp
);

-- copy command to copy order_reviews data
COPY RAW.ORDER_REVIEWS (review_id, order_id, review_score,review_comment_title,review_comment_message,review_creation_date,review_answer_timestamp)
FROM '/data/olist_order_reviews_dataset.csv' DELIMITER ',' CSV HEADER;


-- DDL for orders table mapping to the olist_orders_dataset.csv
create table if not exists RAW.ORDERS
(
    order_id uuid primary key,
    customer_id uuid not null,
    order_status varchar,
    order_purchase_timestamp timestamp,
    order_approved_at timestamp,
    order_delivered_carrier_date timestamp,
    order_delivered_customer_date timestamp,
    order_estimated_delivery_date timestamp
);

-- copy command to copy orderS data
COPY RAW.ORDERS (order_id,customer_id,order_status,order_purchase_timestamp,order_approved_at,order_delivered_carrier_date,order_delivered_customer_date,order_estimated_delivery_date)
FROM '/data/olist_orders_dataset.csv' DELIMITER ',' CSV HEADER;

-- DDL for orders table mapping to the olist_products_dataset.csv
create table if not exists RAW.PRODUCTS
(
    product_id uuid primary key,
    product_category_name varchar,
    product_name_lenght int,
    product_description_lenght int,
    product_photos_qty int,
    product_weight_g int,
    product_length_cm int,
    product_height_cm int,
    product_width_cm int
);

-- copy command to copy products data
COPY RAW.PRODUCTS (product_id,product_category_name,product_name_lenght,product_description_lenght,product_photos_qty,product_weight_g,product_length_cm,product_height_cm,product_width_cm)
FROM '/data/olist_products_dataset.csv' DELIMITER ',' CSV HEADER;


-- DDL for orders table mapping to the olist_sellers_dataset.csv
create table if not exists RAW.SELLERS
(
    seller_id uuid primary key,
    seller_zip_code_prefix varchar not null,
    seller_city varchar not null,
    seller_state varchar

);

-- copy command to copy products data
COPY RAW.SELLERS (seller_id,seller_zip_code_prefix,seller_city,seller_state)
FROM '/data/olist_sellers_dataset.csv' DELIMITER ',' CSV HEADER;



-- DDL for orders table mapping to the olist_product_category_name_translation_dataset.csv
create table if not exists RAW.PRODUCT_CATEGORY_NAME_TRANSLATION
(
    product_category_name varchar,
    product_category_name_english varchar

);

-- copy command to copy products data
COPY RAW.PRODUCT_CATEGORY_NAME_TRANSLATION (product_category_name,product_category_name_english)
FROM '/data/product_category_name_translation.csv' DELIMITER ',' CSV HEADER;









