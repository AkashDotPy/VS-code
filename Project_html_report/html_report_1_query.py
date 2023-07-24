import pandas as pd
from sqlalchemy import create_engine
from jinja2 import Environment, FileSystemLoader
import os
from dotenv import load_dotenv
load_dotenv()

db_url = os.getenv('database')
engine = create_engine(db_url)
conn = engine.connect()

env = Environment(loader=FileSystemLoader('Project_html_report'))
template = env.get_template('template.html')

# Load SQL queries from the CSV file into a list
csv_file_path = "C:\Users\HP\Desktop\VS code\Project_html_report\sql_queries_1.csv"
queries_df = pd.read_csv(csv_file_path)
   
queries_list = queries_df['query'].tolist()

# Fetch data from the database for each query
results_list = []
for query in queries_list:
    result = pd.read_sql_query(query, conn)
    results_list.append(result)
# print(results_list)

html_tables = []
for df in results_list:
    html_table = df.to_html(index=False)
    html_tables.append(html_table)

all_html_tables = '<br>'.join(html_tables)

html = template.render(page_title='Database report',
                       header='Database report in html templete',
                       sub_header1='Description ',
                       description1='The following table shows details about different countries',
                       html_table_1=all_html_tables)

# create html file
with open('report_1.htm', 'w') as f:
    f.write(html)

conn.close()