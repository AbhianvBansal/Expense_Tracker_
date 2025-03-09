# from tkinter import messagebox
# from Interface import Profile, AddIncome, AddExpense, ExpvsTime
import Login
import db_functions
import mysql.connector as mysql
from dotenv import load_dotenv
import os
# Start Page

load_dotenv()

connection = mysql.connect(
    host=os.getenv('MYSQL_HOST', default='localhost'),
    user=os.getenv('MYSQL_USER', default='root'),
    password=os.getenv('MYSQL_PASSWORD', default='abhi@9090'),
    database=os.getenv('MYSQL_DATABASE', default='exptrack')
)
# print("Host:", os.getenv('MYSQL_HOST'), "User:", os.getenv('MYSQL_USER'), "Password:", os.getenv('MYSQL_PASSWORD'), "Database:", os.getenv('MYSQL_DATABASE'))

is_db_initialised = db_functions.check_if_db_initialised(connection)
if not is_db_initialised:
    queries = db_functions.get_initial_queries()
    status = db_functions.execute_queries(queries)
    if status:
        print('DB INITIALISED SUCCESSFULLY')
    else:
        print('ERROR INITIALISING DB')
register = Login.launch()

# A87676
# CA8787
# E1ACAC
# FFD0D0
