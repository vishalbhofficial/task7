import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

# Connected PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres", 
    password="Vishal@3690", # It shows error sometimes but its correct password used 
    host="localhost",   
    port="5432"  
)

# Define SQL query
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product;
"""

# Load data into pandas DataFrame
df = pd.read_sql_query(query, conn)

# Print results
print("Sales Summary:")
print(df)

# Plot
df.plot(kind='bar', x='product', y='revenue', title='Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Revenue')
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

# Close connection
conn.close()

