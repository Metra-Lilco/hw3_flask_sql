import sqlite3

from faker import Faker


con = sqlite3.connect("flask_sql.db")
cur = con.cursor()
create_table_customers = """
CREATE TABLE customers (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    gender VARCHAR(255),
    phone_number VARCHAR(255)
    )
"""
cur.execute(create_table_customers)
