with product_translation as (
    select * -- select columns of interest
      from {{ source('raw_data', 'product_category_name_translation') }}
)

select *
  from product_translation