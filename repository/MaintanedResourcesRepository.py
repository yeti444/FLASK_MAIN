from db.db_conn import db_conn
from models.MaintanedResources import MaintanedResources


def get_all_MaintanedResources():
    conn = db_conn()
    cur = conn.cursor()
    query = "SELECT * FROM maintanedresources;"
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    conn.close()
    MaintanedResources_entries = [MaintanedResources(maintId = entry[0], resourceId = entry[1]) for entry in data]
    return MaintanedResources_entries

def get_one_MaintanedResources(maintId, resourceId):
    conn = db_conn()
    cur = conn.cursor()
    query = "SELECT * FROM maintanedresources WHERE maintId = %s AND resourceId = %s;"
    cur.execute(query, (maintId, resourceId,))
    entry = cur.fetchone()
    cur.close()
    conn.close()
    if entry:
        return MaintanedResources(maintId = entry[0], resourceId = entry[1])
    else: 
        None

def create_MaintanedResources(maintId, resourceId):
    conn = db_conn()
    cur = conn.cursor()
    query = "insert into maintanedresources (maintId, resourceId) values (%s, %s);"
    cur.execute(query, (maintId, resourceId,))
    conn.commit()
    cur.close()
    conn.close()

def update_MaintanedResources(maintId, resourceId):
    conn = db_conn()
    cur = conn.cursor()
    query = "UPDATE maintanedresources SET maintId = %s, resourceId = %s WHERE maintId = %s AND resourceId = %s;"
    cur.execute(query, (maintId, resourceId,))
    conn.commit()
    cur.close()
    conn.close()

def delete_MaintanedResources(maintId, resourceId):
    conn = db_conn()
    cur = conn.cursor()
    query = "delete from maintanedresources WHERE workId = %s AND resourceId = %s;"
    cur.execute(query, (maintId, resourceId,))
    conn.commit()
    cur.close()
    conn.close()