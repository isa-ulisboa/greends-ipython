import mysql.connector
conn = mysql.connector.connect(
    host = 'localhost',
	database = 'dms_INE',
    user = 'root',
    password = 'aziza123'
) 
import pandas as pd
query = ("SELECT NutsID, region_name FROM region WHERE region_level = 4")
result_df = pd.read_sql(query, conn)
conn.close()
