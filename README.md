# Task 7 – Basic Sales Summary using SQLite and Python

# Task Objective

The goal of this task was to extract and visualize basic sales data (like total quantity sold and revenue) from a small SQLite database using Python and SQL.

#Tools Used

- Python
- SQLite (`Postgre` module)
- Pandas
- Matplotlib

---

# What I Did

1. Created a simple SQLite database file named `sales_data`
2. Created a `sales` table with fields:
   - `id`
   - `product` (text)
   - `quantity` (integer)
   - `price` (real)
3. Inserted sample sales records for products like Apple, Banana, Orange, Onion & Ginger
4. Wrote a SQL query in Python to:
   - Group data by product
   - Calculate total quantity and revenue
5. Loaded SQL query result into a Pandas DataFrame
6. Displayed the results in the terminal

