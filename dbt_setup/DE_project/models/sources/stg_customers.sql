with customers as (
    select * -- select columns of interest
      from {{ source('raw_data', 'customers') }}
)

select *
  from customers