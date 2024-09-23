import psycopg2
from models.ScheduledResources import ScheduledResources

def db_conn():
    return psycopg2.connect(database="resourceManagement", host="localhost", user="", password="lenin17", port="5432")

def get_all_ScheduledResources():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM scheduledresources''')
    data = cur.fetchall()
    cur.close()
    conn.close()
    ScheduledResources_entries = [ScheduledResources(workId = entry[0], resourceId = entry[1]) for entry in data]
    return ScheduledResources_entries

def get_one_ScheduledResources(workId, resourceId):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM scheduledresources WHERE workId = {0} AND resourceId = {1}'''.format(workId, resourceId))
    ScheduledResources_entry = cur.fetchone()
    cur.close()
    conn.close()
    if ScheduledResources_entry:
        return ScheduledResources(workId = ScheduledResources_entry[0], resourceId = ScheduledResources_entry[1])
    else: 
        None

def create_ScheduledResources(workId, resourceId):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''insert into scheduledresources (workId, resourceId) values ('{0}', '{1}');'''.format(workId, resourceId))
    conn.commit()
    cur.close()
    conn.close()

def update_ScheduledResources(workId, resourceId):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''UPDATE scheduledresources SET workId = '{0}', resourceId = '{1}' WHERE workId = {0} AND resourceId = {1};'''.format(workId, resourceId))
    conn.commit()
    cur.close()
    conn.close()

def delete_ScheduledResources(workId, resourceId):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''delete from ScheduledResources WHERE workId = {0} AND resourceId = {1} ;'''.format(workId, resourceId))
    conn.commit()
    cur.close()
    conn.close()