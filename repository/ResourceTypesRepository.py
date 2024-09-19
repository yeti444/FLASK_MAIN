import psycopg2
from models.ResourceTypes import ResourceTypes

def db_conn():
    return psycopg2.connect(database="resourceManagement", host="localhost", user="", password="lenin17", port="5432")

def get_all_ResourceTypes():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM resourcetypes''')
    data = cur.fetchall()
    cur.close()
    conn.close()
    ResourceTypes_entries = [ResourceTypes(typeId=entry[0], typeName=entry[1]) for entry in data]
    return ResourceTypes_entries

def get_one_ResourceTypes(typeId):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM resourcetypes WHERE typeid = {0}'''.format(typeId))
    ResourceTypes_entry = cur.fetchone()
    cur.close()
    conn.close()
    if ResourceTypes_entry:
        return ResourceTypes(typeId=ResourceTypes_entry[0], typeName=ResourceTypes_entry[1])
    else: 
        None

def create_ResourceTypes(typeName):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''insert into resourcetypes (typename) values ('{0}') returning typeid;'''.format(typeName))
    new_ResourceTypes_typeId = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return new_ResourceTypes_typeId

def update_ResourceTypes(typeId, typeName):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''UPDATE resourcetypes SET typename = '{0}' WHERE typeid = '{1}' ;'''.format(typeName, typeId))
    conn.commit()
    cur.close()
    conn.close()
    
def delete_ResourceTypes(typeId):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''delete from resourcetypes where typeId = {0} ;'''.format(typeId))
    conn.commit()
    cur.close()
    conn.close()