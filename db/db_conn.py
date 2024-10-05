import psycopg2
import configparser

config = configparser.ConfigParser()
config.read("./db/config.ini")
password_input = config['configuration']['password']

def db_conn():
    return psycopg2.connect(database="resourceManagement", host="localhost", user="", password=password_input, port="5432")