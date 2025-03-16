import streamlit as st



import mysql.connector

mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 database='project1'
)
print(mydb)
mycursor = mydb.cursor(buffered=True)


col = st.sidebar.selectbox('Query Number',['Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20'])
#st.write(col)

if col=='Q1':
    sql_query_1 = """
    SELECT product_id, SUM(quantity * sale_price) AS total_revenue, Category, City
    FROM orders
    GROUP BY product_id
    ORDER BY total_revenue DESC
    LIMIT 10;
    """

# Executing the query
    mycursor.execute(sql_query_1)

# Fetching the results
    results1 = mycursor.fetchall()

    st.header('1.Top 10 highest revenue generating products')
# Printing the results
    for row in results1:
        st.write(f"Product ID: {row[0]}, Total Revenue: {row[1]}, Category: {row[2]}, City: {row[3]}")   
        

elif col=='Q2':
    sql_query_2 = """
    SELECT City, product_id, SUM(Revenue) AS total_revenue, SUM(cost_price) as total_cost,
    (SUM(Revenue) - SUM(cost_price)) / SUM(Revenue) * 100 AS profit_margin
    FROM orders
    GROUP BY City
    ORDER BY profit_margin DESC
    LIMIT 5;
    """

# Executing the query
    mycursor.execute(sql_query_2)

# Fetching the results
    results2 = mycursor.fetchall()

    st.header("2.Top 5 cities with the highest profit margins")

# Printing the results
    for row in results2:
        st.write(f"City: {row[0]}, Product ID: {row[1]}, Total Revenue: {row[2]}, Total_Cost: {row[3]}, profit Margin:{row[4]}")
        

elif col=='Q3':
    sql_query = """
    SELECT Category, SUM(discount) AS total_discount
    FROM Orders
    group by Category
    Order by total_discount  desc;
    """

# Executing the query
    mycursor.execute(sql_query)

# Fetching the results
    results = mycursor.fetchall()

    st.header('3.The total discount given for each category')

# Printing the results
    for row in results:
        st.write(f"Category: {row[0]}, Total Discount: {row[1]}")
        

elif col=='Q4':
    sql_query = """
    SELECT Category, AVG(sale_price) AS Avg_sale_price
    FROM Orders
    group by Category
    Order by Avg_sale_price  desc;
    """

# Executing the query
    mycursor.execute(sql_query)

# Fetching the results
    results = mycursor.fetchall()
    st.header('4.The average sale price per product category')

# Printing the results
    for row in results:
        st.write(f"Category: {row[0]}, Average Sale Price: {row[1]}")
        


elif col=='Q5':
    sql_query = """
    select Region, AVG(sale_price) as Avg_sale_price
    FROM Orders
    group by Region
    Order by Avg_sale_price desc
    Limit 1;"""

    mycursor.execute(sql_query)

    results = mycursor.fetchall()
    st.header('5.The region with the highest average sale price')

    for row in results:
        #st.write(print(f"Region: {row[0]}, Average Sale Price: {row[1]}"))
        st.write(f"Region: {row[0]}, Average Sale Price: {row[1]}")

elif col=='Q6':
    sql_query = """
    select Category, SUM(profit) as Total_profit
    From Orders
    group by Category
    Order by Total_profit;"""

    mycursor.execute(sql_query)

    results = mycursor.fetchall()
    st.header('6.The total profit per category')

    for row in results:
        st.write(f"Category: {row[0]}, Total_Profit: {row[1]}")

elif col=='Q7':
    sql_query ="""
    select Segment, SUM(Quantity) as Total_order_Quantity
    From Orders
    group by Segment
    Order by Total_order_Quantity desc
    Limit 3;"""

    mycursor.execute(sql_query)

    results = mycursor.fetchall()
    st.header('7.The top 3 segments with the highest quantity of orders')

    for row in results:
        st.write(f"Segment: {row[0]}, Total_order_Quantity: {row[1]}")

elif col=='Q8':
    sql_query = """
    select Region, AVG(discount_percent) as  Avg_discount_percent
    From Orders
    group by Region
    order by Avg_discount_percent""" 

    mycursor.execute(sql_query)

    results = mycursor.fetchall()
    st.header('8. The average discount percentage given per region')

    for row in results:
        st.write(f"Region: {row[0]}, Avg Discount Percent: {row[1]}")

elif col=='Q9':
    sql_query ="""select Category, SUM(Quantity*profit) as Total_profit
    From Orders
    group by Category
    order by Total_profit
    limit 1;"""

    mycursor.execute(sql_query)

    results = mycursor.fetchall()
    st.header('9. The product category with the highest total profit')

    for row in results:
        st.write(f"Category: {row[0]}, Total Profit: {row[1]}")

elif col=='Q10':
    sql_query ="""select Year(order_date), SUM(Revenue) as Total_Revenue
    From Orders
    group by Year(order_date)
    order by Total_Revenue
    """

    mycursor.execute(sql_query)

    results = mycursor.fetchall()
    st.header('10. The total revenue generated per year')

    for row in results:
        st.write(f"Year: {row[0]}, Total_Revenue: {row[1]}")

elif col=='Q11':
    sql_query = """select Year(order_date), sub_category, SUM(Quantity) as Total_orders
    From Orders
    Where sub_category = 'Tables'
    group by Year(order_date)
    order by Year(order_date)"""

    mycursor.execute(sql_query)

    results = mycursor.fetchall()
    st.header('11. Total no of tables ordered in each year')

    for row in results:
        st.write(f"Year: {row[0]}, Product: {row[1]} Total_orders: {row[2]}")

elif col=='Q12':
    sql_query = """select City, SUM(Quantity * profit) as Highest_profit
    From orders
    group by City
    Order by Highest_profit desc
    limit 1"""

    mycursor.execute(sql_query)

    results = mycursor.fetchall()
    st.header('12. City that has got highest profit')

    for row in results:
        st.write(f"City: {row[0]}, Highest profit: {row[1]}")

elif col=='Q13':
    sql_query = """select City, SUM(Quantity) as total_quantity, sub_category
    From orders
    where sub_category = 'Chairs'
    group by City
    order by total_quantity desc
    limit 5"""

    mycursor.execute(sql_query)

    results = mycursor.fetchall()
    st.header('13. Top 5 cities that has ordered most number of Chairs')

    for row in results:
        st.write(f"City: {row[0]}, Total_Quantity: {row[1]}, product: {row[2]}")

elif col=='Q14':
    sql_query = """select sub_category, product_id, SUM(Quantity * profit) as Total_profit
    From orders
    group by sub_category
    order by Total_profit desc
    Limit 1"""

    mycursor.execute(sql_query)

    results = mycursor.fetchall()
    st.header('14. The most profitable sub_category product')

    for row in results:
        st.write(f"sub_category: {row[0]}, product_id: {row[1]}, Total_profit: {row[2]}")


elif col == 'Q15':
    sql_query = """select State, sub_category, SUM(Quantity) as Total_orders
    From orders
    group by State
    order by Total_orders desc
    Limit 1"""

    mycursor.execute(sql_query)

    results = mycursor.fetchall()

    st.header('15. The state that has ordered most number of products')

    for row in results:
        st.write(f"State: {row[0]}, sub_category: {row[1]}, Total_orders: {row[2]}")

elif col == 'Q16':
    sql_query = """select Region, SUM(Quantity * profit) as Total_profit
    From orders
    group by Region
    order by Total_profit desc
    Limit 1"""

    mycursor.execute(sql_query)

    results = mycursor.fetchall()

    st.header('16.The region with highest profit')

    for row in results:
        st.write(f"Region: {row[0]}, Total_Profit: {row[1]}")

elif col == 'Q17':
    sql_query = """select product_id, sub_category, SUM(Quantity * discount) as Total_discount
    From orders
    group by product_id
    order by Total_discount desc"""

    mycursor.execute(sql_query)

    results = mycursor.fetchall()

    st.header('17. Discount given for each product')

    for row in results:
        st.write(f"Product ID: {row[0]}, Product Name: {row[1]}, Total_discount: {row[2]}")

elif col == 'Q18':
    sql_query = """select Year(order_date), SUM(Quantity * profit) as Total_profit
    From orders
    group by Year(order_date)
    order by Total_profit desc"""

    mycursor.execute(sql_query)

    results = mycursor.fetchall()

    st.header('18. Total  profit generated per year')

    for row in results:
        st.write(f"Year: {row[0]}, Total_profit: {row[1]}")

elif col == 'Q19':
    sql_query = """select City, sub_category, SUM(Quantity) as total
    From orders
    where sub_category = 'Bookcases'
    group by City
    order by total desc
    limit 1"""

    mycursor.execute(sql_query)

    results = mycursor.fetchall()

    st.header('19. The city that has ordered most number of book cases')

    for row in results:
        st.write(f"City: {row[0]}, Product: {row[1]}, total: {row[2]}")

else:
    sql_query = """select State, Avg(Revenue) as Average
    From orders
    group by State
    order by Average desc"""

    mycursor.execute(sql_query)

    results = mycursor.fetchall()

    st.header('20. Average revenue of each state')

    for row in results:
        st.write(f"State: {row[0]}, Average: {row[1]}")