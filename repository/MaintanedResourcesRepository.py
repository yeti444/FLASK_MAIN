import psycopg2
from models.MaintanedResources import MaintanedResources

def db_conn():
    return psycopg2.connect(database="resourceManagement", host="localhost", user="", password="lenin17", port="5432")

def get_all_MaintanedResources():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM maintanedresources''')
    data = cur.fetchall()
    cur.close()
    conn.close()
    MaintanedResources_entries = [MaintanedResources(maintId = entry[0], resourceId = entry[1]) for entry in data]
    return MaintanedResources_entries

def get_one_MaintanedResources(maintId, resourceId):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM maintanedresources WHERE maintId = {0} AND resourceId = {1}'''.format(maintId, resourceId))
    MaintanedResources_entry = cur.fetchone()
    cur.close()
    conn.close()
    if MaintanedResources_entry:
        return MaintanedResources(maintId = MaintanedResources_entry[0], resourceId = MaintanedResources_entry[1])
    else: 
        None

def create_MaintanedResources(maintId, resourceId):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''insert into maintanedresources (maintId, resourceId) values ('{0}', '{1}');'''.format(maintId, resourceId))
    conn.commit()
    cur.close()
    conn.close()

def update_MaintanedResources(maintId, resourceId):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''UPDATE maintanedresources SET maintId = '{0}', resourceId = '{1}' WHERE maintId = {0} AND resourceId = {1};'''.format(maintId, resourceId))
    conn.commit()
    cur.close()
    conn.close()

def delete_MaintanedResources(maintId, resourceId):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''delete from maintanedresources WHERE workId = {0} AND resourceId = {1} ;'''.format(maintId, resourceId))
    conn.commit()
    cur.close()
    conn.close()