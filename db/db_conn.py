import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

password_input = os.getenv('DB_PASSWORD')
username_input = os.getenv('DB_USERNAME')

def db_conn():
    return psycopg2.connect(
        database="resourceManagement",
        host="localhost",
        user=username_input,
        password=password_input,
        port="5432"
    )
