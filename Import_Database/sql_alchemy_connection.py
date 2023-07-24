import pandas as pd
from sqlalchemy import create_engine


db_url = 'postgresql+psycopg2://avnadmin:AVNS_5AW5L8ukW4C8IIlVKGD@pg-3ea0cb8c-datacloudgaze-e65f.aivencloud.com:24464/defaultdb'
engine = create_engine(db_url)

conn = engine.connect()

query1 = "SELECT * FROM sakila.country;"
query2 = "SELECT * FROM sakila.persons;"

# Fetch data from the database
data1 = pd.read_sql_query(query1, conn)
data2 = pd.read_sql_query(query2, conn)

# Generate HTML tables
html_table1 = data1.to_html(index=False)
html_table2 = data2.to_html(index=False)

# Combine HTML tables
combined_html = f"{html_table1}\n{html_table2}"

# Save combined HTML to a file
with open('sqlalchemy_combined_tables.html', 'w') as file:
    file.write(combined_html)

conn.close()    