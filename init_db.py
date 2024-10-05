import psycopg2

conn = psycopg2.connect(database="resourceManagement", host="localhost", user="purgetrapscorp", password="lenin17", port="5432")
cur = conn.cursor()

cur.execute('''SELECT * FROM RESOURCETYPES''')
conn.commit()

cur.close()
conn.close()