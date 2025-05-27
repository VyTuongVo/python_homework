import pandas as pd
import sqlite3
import matplotlib.pyplot as plt


#Task 1
conn = sqlite3.connect('../db/lesson.db')

#Copy and pasted from the task
query = """
SELECT last_name, SUM(price * quantity) AS revenue FROM employees e JOIN orders o ON e.employee_id = o.employee_id JOIN line_items l ON o.order_id = l.order_id JOIN products p ON l.product_id = p.product_id GROUP BY e.employee_id;
"""
employee_results = pd.read_sql_query(query, conn)
conn.close()
print(employee_results)

plt.figure(figsize=(10,6))
plt.bar(employee_results['last_name'], employee_results['revenue'])
plt.title('Revenue of Employee')
plt.xlabel('Employee Last Name')
plt.ylabel('Employee Revenue')
plt.xticks(rotation=90, ha='right') # This allow full view of the name as it would stand on top of each other before
plt.show()

#Task 2
