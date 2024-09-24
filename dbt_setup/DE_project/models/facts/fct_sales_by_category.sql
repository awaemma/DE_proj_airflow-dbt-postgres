/**
 I have referenced the intermidiate int_sales_by_category table and the staging
 stg_product_category_name_translation table so I can retrieve the product category English name
**/

{{ config(materialized='table') }}

with sales as (
    select
       pc.product_category_name_english as product_category_name
      ,sc.total_sales
    from
        {{ref('int_sales_by_category')}} sc 
    join
        {{ref('stg_product_category_name_translation')}} pc
    on
      sc.product_category_name = pc.product_category_name
)
select
   *
from
   sales

