with products as (
    select * -- select columns of interest
      from {{ source('raw_data', 'products') }}
)

select *
  from products