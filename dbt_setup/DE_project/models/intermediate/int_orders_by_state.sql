
/** orders by state here means the customer location where the orders were place.
    The information we require are in the customers and orders table.
**/
with orders_by_state as (
    select
       o.order_id,
       c.customer_state
    from
        {{ref('stg_orders')}} o
    join 
        {{ref('stg_customers')}} c
    on
       o.customer_id = c.customer_id
        
)

select
   customer_state
  ,count(order_id) as orders_per_state
from
   orders_by_state
group by 
   customer_state