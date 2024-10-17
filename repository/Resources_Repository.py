from db.db_conn import db_conn
from models.Resources import Resources


def get_all_Resources():
    conn = db_conn()
    cur = conn.cursor()
    query = "SELECT * FROM resources;"
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    conn.close()
    UserData_entries = [Resources(resourceId = entry[0], name = entry[1], typeId = entry[2], info = entry[3], createDate=entry[4]) for entry in data]
    return UserData_entries

def get_one_Resources(resourceId):
    conn = db_conn()
    cur = conn.cursor()
    query = "SELECT * FROM resources WHERE resourceId = %s;"
    cur.execute(query, (resourceId,))
    entry = cur.fetchone()
    cur.close()
    conn.close()
    if entry:
        return Resources(resourceId = entry[0], name = entry[1], typeId = entry[2], info = entry[3], createDate=entry[4])
    else: 
        return None

def create_Resources(name, typeId, info):
    conn = db_conn()
    cur = conn.cursor()
    query = "insert into resources (name, typeId, info) values (%s, %s, %s) returning resourceId;"
    cur.execute(query, (name, typeId, info,))
    new_Resources_resourceId = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return new_Resources_resourceId

def update_Resources(resourceId, name, typeId, info):
    conn = db_conn()
    cur = conn.cursor()
    query = "UPDATE resources SET name = %s, typeId = %s, info = %s WHERE resourceId = %s;"
    cur.execute(query, (name, typeId, info, resourceId))
    conn.commit()
    cur.close()
    conn.close()
    
def delete_Resources(resourceId):
    conn = db_conn()
    cur = conn.cursor()
    query = "delete from resources where resourceId = %s;"
    cur.execute(query, (resourceId,))
    conn.commit()
    cur.close()
    conn.close()
