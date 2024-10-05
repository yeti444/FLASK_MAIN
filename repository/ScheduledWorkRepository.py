from db.db_conn import db_conn
from models.ScheduledWork import ScheduledWork


def get_all_ScheduledWork():
    conn = db_conn()
    cur = conn.cursor()
    query = "SELECT * FROM scheduledwork;"
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    conn.close()
    ScheduledWork_entries = [ScheduledWork(workId = entry[0], userId = entry[1], fromDate = entry[2], duration = entry[3], createDate = entry[4]) for entry in data]
    return ScheduledWork_entries

def get_one_ScheduledWork(workId):
    conn = db_conn()
    cur = conn.cursor()
    query = "SELECT * FROM scheduledwork WHERE workId = %s;"
    cur.execute(query, (workId,))
    entry = cur.fetchone()
    cur.close()
    conn.close()
    if entry:
        return ScheduledWork(workId = entry[0], userId = entry[1], fromDate = entry[2], duration = entry[3], createDate = entry[4])
    else: 
        None

def create_ScheduledWork(userId, fromDate, duration):
    conn = db_conn()
    cur = conn.cursor()
    query = "insert into scheduledwork (userId, fromDate, duration) values (%s, %s, %s) returning workId;"
    cur.execute(query, (userId, fromDate, duration,))
    new_ScheduledWork_workId = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return new_ScheduledWork_workId

def update_ScheduledWork(workId, userId, fromDate, duration):
    conn = db_conn()
    cur = conn.cursor()
    query = "'''UPDATE scheduledwork SET userId = %s, fromDate = %s, duration = %s WHERE workId = %s;"
    cur.execute(query, (userId, fromDate, duration, workId,))
    conn.commit()
    cur.close()
    conn.close()

def delete_ScheduledWork(workId):
    conn = db_conn()
    cur = conn.cursor()
    query = "delete from scheduledwork where workId = %s;"
    cur.execute(query, (workId,))
    conn.commit()
    cur.close()
    conn.close()