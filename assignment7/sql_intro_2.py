#Task 6

import pandas as pd
import sqlite3

connection = sqlite3.connect("../db/lesson.db")

query = """
SELECT 
    line_items.line_item_id, 
    line_items.quantity, 
    line_items.product_id, 
    products.product_name, 
    products.price
FROM 
    line_items
JOIN 
    products
ON 
    line_items.product_id = products.product_id
"""
df = pd.read_sql_query(query, connection)

print("\nFirst 5 rows of data:")
print(df.head(5))

df['total'] = df['quantity'] * df['price']
print("\nFirst 5 rows to see 'total':")
print(df.head(5))


general = df.groupby('product_id').agg({
    'line_item_id': 'count',    
    'total': 'sum',             
    'product_name': 'first'     
}).reset_index()

print("\nFirst 5 rows after groupby")
print(general.head(5))

general = general.sort_values(by='product_name')
general.to_csv("order_summary.csv", index=False)



