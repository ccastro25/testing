import datetime
import mysql.connector
from sqlalchemy import create_engine
import pandas as pd

cnx = mysql.connector.connect(user='scott', database='employees')
cursor = cnx.cursor()

query = ("SELECT first_name, last_name, hire_date FROM employees "
         "WHERE hire_date BETWEEN %s AND %s")

hire_start = datetime.date(1999, 1, 1)
hire_end = datetime.date(1999, 12, 31)

cursor.execute(query, (hire_start, hire_end))

for (first_name, last_name, hire_date) in cursor:
  print("{}, {} was hired on {:%d %b %Y}".format(
    last_name, first_name, hire_date))

cursor.close()
cnx.close()



db_connection_str = 'mysql+pymysql://mysql_user:mysql_password@mysql_host/mysql_db'
db_connection = create_engine(db_connection_str)

df = pd.read_sql('SELECT * FROM table_name', con=db_connection)
db_connection.close()