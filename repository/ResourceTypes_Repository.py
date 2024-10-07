from db.db_conn import db_conn
from models.ResourceTypes import ResourceTypes


def get_all_ResourceTypes():
    conn = db_conn()
    cur = conn.cursor()
    query = "SELECT * FROM resourcetypes;"
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    conn.close()
    ResourceTypes_entries = [ResourceTypes(typeId=entry[0], typeName=entry[1]) for entry in data]
    return ResourceTypes_entries

def get_one_ResourceTypes(typeId):
    conn = db_conn()
    cur = conn.cursor()
    query = "SELECT * FROM resourcetypes WHERE typeid = %s;"
    cur.execute(query, (typeId,))
    entry = cur.fetchone()
    cur.close()
    conn.close()
    if entry:
        return ResourceTypes(typeId=entry[0], typeName=entry[1])
    else: 
        None

def create_ResourceTypes(typeName):
    conn = db_conn()
    cur = conn.cursor()
    query = "insert into resourcetypes (typename) values (%s) returning typeid;"
    cur.execute(query, (typeName,))
    new_ResourceTypes_typeId = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return new_ResourceTypes_typeId

def update_ResourceTypes(typeId, typeName):
    conn = db_conn()
    cur = conn.cursor()
    query = "UPDATE resourcetypes SET typename = %s WHERE typeid = %s;"
    cur.execute(query, (typeName, typeId,))
    conn.commit()
    cur.close()
    conn.close()
    
def delete_ResourceTypes(typeId):
    conn = db_conn()
    cur = conn.cursor()
    query = "delete from resourcetypes where typeId = %s;"
    cur.execute(query, (typeId,))
    conn.commit()
    cur.close()
    conn.close()