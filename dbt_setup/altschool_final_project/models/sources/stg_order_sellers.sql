with order_sellers as (
    select * -- select columns of interest
      from {{ source('raw_data', 'sellers') }}
)

select *
  from order_sellers