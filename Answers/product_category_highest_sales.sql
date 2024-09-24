-- health beauty product category has the highest sales at 1,258,681

SELECT product_category_name as Product_Name
       ,total_sales as Total_Sales
 FROM `alt-school-project-425214.transformed.fct_sales_by_category` 
 ORDER BY total_sales DESC
 LIMIT 1