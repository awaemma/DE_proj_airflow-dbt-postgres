-- this is a direct reference to the intermediate delivery time table
{{ config(materialized='table') }}

with orders_by_state as (
    select
       *
    from
        {{ref('int_orders_by_state')}}    
)
select
   *
from
   orders_by_state

