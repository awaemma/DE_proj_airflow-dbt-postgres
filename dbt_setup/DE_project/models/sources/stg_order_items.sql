with order_items as (
    select * -- select columns of interest
      from {{ source('raw_data', 'order_items') }}
)

select *
  from order_items