import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

host_input = os.getenv('DB_HOST')
port_input = os.getenv('DB_PORT')

password_input = os.getenv('DB_PASSWORD')
username_input = os.getenv('DB_USERNAME')


def db_conn():
    return psycopg2.connect(
        database="resourceManagement",
        host=host_input,
        user=username_input,
        password=password_input,
        port=port_input
    )
