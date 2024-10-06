import psycopg2
import configparser

config = configparser.ConfigParser()
config.read("./db/config.ini")
password_input = config['configuration']['password']
username_input = config['configuration']['username']

def db_conn():
    return psycopg2.connect(database="resourceManagement", host="localhost", user=username_input, password=password_input, port="5432")