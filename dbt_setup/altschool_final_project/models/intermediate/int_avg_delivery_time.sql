/** Given the requirement to calculate the average delivery time for each order,
    we have to get the delivery time for each order first.
    I have used the difference between when customer confirmed receipt (order_delivered_customer_date)
    and when order purchase was made (order_purchase_timestamp).
    In addition, I have also added for estimated delivery time just to check how well we have performed againt when customer actually received it.
    - More so, we have filtered to only orders with order_status as 'delivered'.
**/

with delivery_time as (
    select
       order_id
     ,order_purchase_timestamp
     ,order_delivered_customer_date
     ,order_estimated_delivery_date
    from
        {{ref('stg_orders')}}
    where
       order_status = 'delivered'      
)
select
   order_id
  ,TIMESTAMP_DIFF(order_delivered_customer_date,order_purchase_timestamp,DAY) as customer_delivery_time
  ,TIMESTAMP_DIFF(order_estimated_delivery_date,order_purchase_timestamp,DAY) as estimated_delivery_time
from
   delivery_time

