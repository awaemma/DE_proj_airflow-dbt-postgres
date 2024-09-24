-- this is a direct reference to the intermediate delivery time table
{{ config(materialized='table') }}

with fct_delivery_time as (
    select
       *
    from
        {{ref('int_avg_delivery_time')}}    
)
select
   *
from
   fct_delivery_time

