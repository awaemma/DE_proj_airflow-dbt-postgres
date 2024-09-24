-- SP state has the highest number of orders at 41,746 orders

SELECT customer_state as State
       ,orders_per_state
 FROM `alt-school-project-425214.transformed.fct_orders_by_state` 
 ORDER BY orders_per_state DESC
LIMIT 1