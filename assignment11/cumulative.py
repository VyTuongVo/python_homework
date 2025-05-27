import pandas as pd
import sqlite3
import matplotlib.pyplot as plt


#Task 2
conn = sqlite3.connect('../db/lesson.db')

#Copy and pasted from the task --> This is from task 1
query = """
SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id;
"""
employee_results = pd.read_sql_query(query, conn)
conn.close()
#print(employee_results)
df = employee_results
print(df)

def cumulative(row):
   totals_above = df['total_price'][0:row.name+1]
   return totals_above.sum()

df['cumulative'] = df.apply(cumulative, axis=1)

print(df)


plt.plot(df["order_id"], df["cumulative"], linestyle = "-")
plt.title('Cumulative Revenue VS Orders')
plt.xlabel('Order ID')
plt.ylabel('Cumulative Revenue')
plt.show()

##########################
#Task 3
import plotly.express as px
import plotly.data as pldata
df = pldata.wind(return_type='pandas')

print(df.head(10))
print(df.tail(10))
df['strength'] = df['strength'].str.replace(r'[^0-9.]', '', regex=True).astype(float)

#print(df.head(10)) #solved check!

fig = px.scatter(df, x='strength', y='frequency', color='direction',
                 title='Strength VS Frequency by Direction')

fig.write_html('wind.html') # Saving to HTML file


#with open('wind.html', 'r') as file:
#    read_html = file.read()

#read_html[:500]

# Can find it in file as and it is avaiable in folder as wind.html

