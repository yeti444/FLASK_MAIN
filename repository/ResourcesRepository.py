import psycopg2
from models.Resources import Resources

def db_conn():
    return psycopg2.connect(database="resourceManagement", host="localhost", user="", password="lenin17", port="5432")

def get_all_Resources():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM resources''')
    data = cur.fetchall()
    cur.close()
    conn.close()
    UserData_entries = [Resources(resourceId = entry[0], name = entry[1], typeId = entry[2], info = entry[3], createDate=entry[4]) for entry in data]
    return UserData_entries

def get_one_Resources(resourceId):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM resources WHERE resourceId = {0}'''.format(resourceId))
    Resources_entry = cur.fetchone()
    cur.close()
    conn.close()
    if Resources_entry:
        return Resources(resourceId = Resources_entry[0], name = Resources_entry[1], typeId = Resources_entry[2], info = Resources_entry[3], createDate=Resources_entry[4])
    else: 
        None

def create_Resources(name, typeId, info):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''insert into resources (name, typeId, info) values ('{0}', {1}, '{2}') returning resourceId;'''.format(name, typeId, info))
    new_Resources_resourceId = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return new_Resources_resourceId

def update_Resources(resourceId, name, typeId, info):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''UPDATE resources SET name = '{0}', typeId = {1}, info = '{2}' WHERE resourceId = {3} ;'''.format(resourceId, name, typeId, info))
    conn.commit()
    cur.close()
    conn.close()
    
def delete_Resources(resourceId):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''delete from resources where resourceId = {0} ;'''.format(resourceId))
    conn.commit()
    cur.close()
    conn.close()
