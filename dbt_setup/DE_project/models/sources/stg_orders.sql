with orders as (
    select * -- select columns of interest
      from {{ source('raw_data', 'orders') }}
)

select *
  from orders