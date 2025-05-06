import sqlite3

conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

##################################################
#Task 1

#Here is where I will place the SQL code
## Sum price to number to get total
## Then  I would join
#Then group by orderID  then order by
query = """
SELECT 
    o.order_id, 
    SUM(p.price * li.quantity) AS total_price    
FROM orders o
JOIN line_items li ON o.order_id = li.order_id
JOIN products p ON li.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
LIMIT 5;
"""

cursor.execute(query)
results = cursor.fetchall()

# Printing solotuion --> this will print out a table for easier visualization
print("Order ID  |  Total Price")
print("----------------------")
for row in results:
    print(f"{row[0]:>8}  |  ${row[1]:.2f}")



##################################################
#Task 2

"""
Prompt:

For each customer, find the average price of their orders. 
This can be done with a subquery. You compute the price of each order as in part 1, 
but you return the customer_id and the total_price.  
That's the subquery. You need to return the total price using AS total_price, 
and you need to return the customer_id with AS customer_id_b, for reasons that 
will be clear in a moment.  In your main statement, you left join the customer table with the results of 
the subquery, using ON customer_id = customer_id_b.  You aliased the customer_id column 
in the subquery so that the column names wouldn't collide.  Then group by customer_id -- this GROUP 
BY comes after the subquery -- and get the average of the total price of the customer orders.  
Return the customer name and the average_total_price.
"""

query = """
SELECT 
    c.customer_name,
    AVG(order_totals.total_price) AS aver_total_price 
FROM customers c
LEFT JOIN (
    SELECT 
        o.customer_id AS customer_id_b,
        SUM(p.price * li.quantity) AS total_price
    FROM orders o
    JOIN line_items li ON o.order_id = li.order_id
    JOIN products p ON li.product_id = p.product_id
    GROUP BY o.order_id
) AS order_totals
ON c.customer_id = order_totals.customer_id_b
GROUP BY c.customer_id;
"""

cursor.execute(query)
results = cursor.fetchall()

#Print solution
print("\nCustomer Name  |  Average Total Price")
print("-----------------------------------")
for row in results:
    name = row[0]              # Taking name from each row
    total = row[1]             # taking how iuch how much the order is (can be None)

    # Format the name to be left-aligned in a field of 20 characters
    formatted_name = f"{name:<20}"

    if total is not None:
        formatted_total = f"${total:.2f}"
        print(f"{formatted_name}  -  {formatted_total}")
    else:
        # if there is no total, then I would give No order
        print(f"{formatted_name} - No orders")

#Task 3:

'''
You want to create a new order for the customer named Perez and Sons.  The employee creating the order is Miranda Harris.  The customer wants 10 of each of the 5 least expensive products.  You first need to do a SELECT statement to retrieve the customer_id, another to retrieve the product_ids of the 5 least expensive products, and another to retrieve the employee_id.  Then, you create the order record and the 5 line_item records comprising the order.  You have to use the customer_id, employee_id, and product_id values you obtained from the SELECT statements. You have to use the order_id for the order record you created in the line_items records. The inserts must occur within the scope of one transaction. Then, using a SELECT with a JOIN, print out the list of line_item_ids for the order along with the quantity and product name for each.

You want to make sure that the foreign keys in the INSERT statements are valid.  So, add this line to your script, right after the database connection:

conn.execute("PRAGMA foreign_keys = 1")
In general, when creating a record, you don't want to specify the primary key.  So leave that column name off your insert statements.  SQLite will assign a unique primary key for you.  But, you need the order_id for the order record you insert to be able to insert line_item records for that order.  You can have this value returned by adding the following clause to the INSERT statement for the order:

RETURNING order_id
Deliverable:

Get this working in sqlcommand. (Note that sqlcommand does not provide a way to begin and end transactions, so for sqlcommand, the creation of the order and line_item records are separate transactions.)
Use sqlcommand to delete the line_items records for the order you created. (This is one delete statement.) Delete also the order record you created.
Add statements for the complete transaction and the subsequent SELECT statement into advanced_py.sql, and to print out the result of the SELECT.
Test your program.
'''
order_id = None

try: 
    conn.execute("BEGIN")
    conn.execute("PRAGMA foreign_keys = 1")

    #I need to be able to the customer's Id which in this case is 'Perez and Sons'

    cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'")
    customer_id = cursor.fetchone()
    if not customer_id: 
        raise ValueError("Can't find customer")  # If you can find customer_id, print out can't find custometr
    customer_id = customer_id[0]

    #Need to get employee who is Miranda Harris
    #I had trouble finding uding full name so iusing first and last name to find the 
    cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris'")
    employee_id = cursor.fetchone()
    if not employee_id: 
        raise ValueError("Employee not found")
    employee_id = employee_id[0]


    cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
    product_ids = [row[0] for row in cursor.fetchall()]
    if not product_ids:
        raise ValueError("No products found")

    #Inserting new ordedr
    cursor.execute("""
        INSERT INTO orders (customer_id, employee_id)
        VALUES (?, ?)
        RETURNING order_id
    """, (customer_id, employee_id))
    order_id = cursor.fetchone()[0]

    # Insert line_items
    for id in product_ids: 
        cursor.execute("""
            INSERT INTO line_items (order_id, product_id, quantity)
            VALUES (?, ?, 10)
        """, (order_id, id))

    conn.commit()
    #Checking point. 
    print(f"Order created successfully, order ID number is {order_id}")

except Exception as e:
    conn.rollback()
    print("Transaction failed:", e)

if order_id:
    print("\nLine Items for New Order:")
    cursor.execute("""
        SELECT li.line_item_id, li.quantity, p.product_name
        FROM line_items li
        JOIN products p ON li.product_id = p.product_id
        WHERE li.order_id = ?
    """, (order_id,))
    line_items = cursor.fetchall()

    print("Line Item ID | Quantity | Product Name")
    print("--------------------------------------")
    for item in line_items:
        print(f"{item[0]:>12} | {item[1]:>8} | {item[2]}")
else:
    print("No order was created so no display can be return")


#Task 4 -> with more than 5 orders

query = """
SELECT 
    e.first_name,
    e.last_name,
    e.employee_id,
    COUNT(o.order_id) AS order_count
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
GROUP BY e.employee_id, e.first_name, e.last_name
HAVING COUNT(o.order_id) > 5;
"""

cursor.execute(query)
results = cursor.fetchall()

# Printing the result
print("Employees with more than 5 orders:")
for row in results:
    print(f"ID: {row[2]}, Name: {row[1]} {row[0]}, Orders: {row[3]}")


conn.close()
