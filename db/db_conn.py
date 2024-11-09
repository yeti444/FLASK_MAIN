import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

host_input = os.getenv('DB_HOST')
port_input = os.getenv('DB_PORT')
username_input = os.getenv('DB_USERNAME')
password_input = os.getenv('DB_PASSWORD')

if not host_input:
    raise ValueError("No DB_HOST set in your .env file.")
if not port_input:
    raise ValueError("No DB_PORT set in your .env file.")
if not username_input:
    raise ValueError("No DB_USERNAME set in your .env file.")
if not password_input:
    raise ValueError("No DB_PASSWORD set in your .env file.")

def db_conn():
    return psycopg2.connect(
        database="resourceManagement",
        host=host_input,
        user=username_input,
        password=password_input,
        port=port_input
    )
