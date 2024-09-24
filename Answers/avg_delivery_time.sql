/**
The average delivery time based on the customer delivery date is 12 days.
However, the average estimated delivery date is 23 days.
This is an indication that orders are delivered before the estimated time in general.
**/
SELECT ROUND(AVG(customer_delivery_time),0) as customer_avg_delivery_time
      ,ROUND(AVG(estimated_delivery_time),0) as estimated_avg_delivery_time
FROM `alt-school-project-425214.transformed.fct_avg_delivery_time`