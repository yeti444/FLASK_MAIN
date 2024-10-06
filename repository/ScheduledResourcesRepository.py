from db.db_conn import db_conn
from models.ScheduledResources import ScheduledResources, ScheduledResources_time


def get_all_ScheduledResources():
    conn = db_conn()
    cur = conn.cursor()
    query = "SELECT * FROM scheduledresources;"
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    conn.close()
    ScheduledResources_entries = [ScheduledResources(workId = entry[0], resourceId = entry[1]) for entry in data]
    return ScheduledResources_entries

def get_all_ScheduledResources_time():
    conn = db_conn()
    cur = conn.cursor()
    query = """select sr.workid, sr.resourceid, sw.fromdate, sw.duration from scheduledresources sr
            inner join scheduledwork sw
            on sr.workid = sw.workid;"""
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    conn.close()
    ScheduledResources_time_entries = [ScheduledResources_time(workId = entry[0], resourceId = entry[1], fromdate=entry[2], duration=entry[3]) for entry in data]
    return ScheduledResources_time_entries

def get_one_ScheduledResources(workId, resourceId):
    conn = db_conn()
    cur = conn.cursor()
    query = "SELECT * FROM scheduledresources WHERE workId = %s AND resourceId = %s;"
    cur.execute(query, (workId, resourceId,))
    entry = cur.fetchone()
    cur.close()
    conn.close()
    if entry:
        return ScheduledResources(workId = entry[0], resourceId = entry[1])
    else: 
        None

def create_ScheduledResources(workId, resourceId):
    conn = db_conn()
    cur = conn.cursor()
    query = "insert into scheduledresources (workId, resourceId) values (%s, %s);"
    cur.execute(query, (workId, resourceId,))
    conn.commit()
    cur.close()
    conn.close()

def update_ScheduledResources(workId, resourceId):
    conn = db_conn()
    cur = conn.cursor()
    query = "UPDATE scheduledresources SET workId = %s, resourceId = %s WHERE workId = %s AND resourceId = %s;"
    cur.execute(query, (workId, resourceId,))
    conn.commit()
    cur.close()
    conn.close()

def delete_ScheduledResources(workId, resourceId):
    conn = db_conn()
    cur = conn.cursor()
    query = "delete from ScheduledResources WHERE workId = %s AND resourceId = %s;"
    cur.execute(query, (workId, resourceId,))
    conn.commit()
    cur.close()
    conn.close()