import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()




"""
DB_HOST=
DB_PORT=5432
DB_USERNAME=
DB_PASSWORD=
"""

host_input = os.getenv('DB_HOST')
port_input = os.getenv('DB_PORT')
username_input = os.getenv('DB_USERNAME')
password_input = os.getenv('DB_PASSWORD')


def db_conn():
    return psycopg2.connect(
        database="resourceManagement",
        host=host_input,
        user=username_input,
        password=password_input,
        port=port_input
    )
