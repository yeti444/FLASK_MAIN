import psycopg2
from models.ScheduledWork import ScheduledWork

def db_conn():
    return psycopg2.connect(database="resourceManagement", host="localhost", user="", password="lenin17", port="5432")

def get_all_ScheduledWork():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM scheduledwork''')
    data = cur.fetchall()
    cur.close()
    conn.close()
    ScheduledWork_entries = [ScheduledWork(workId = entry[0], userId = entry[1], fromDate = entry[2], duration = entry[3], createDate = entry[4]) for entry in data]
    return ScheduledWork_entries

def get_one_ScheduledWork(workId):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM scheduledwork WHERE workId = {0}'''.format(workId))
    ScheduledWork_entry = cur.fetchone()
    cur.close()
    conn.close()
    if ScheduledWork_entry:
        return ScheduledWork(workId = ScheduledWork_entry[0], userId = ScheduledWork_entry[1], fromDate = ScheduledWork_entry[2], duration = ScheduledWork_entry[3], createDate = ScheduledWork_entry[4])
    else: 
        None

def create_ScheduledWork(userId, fromDate, duration):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''insert into scheduledwork (userId, fromDate, duration) values ('{0}', '{1}', '{2}') returning workId;'''.format(userId, fromDate, duration))
    new_ScheduledWork_workId = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return new_ScheduledWork_workId

def update_ScheduledWork(workId, userId, fromDate, duration):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''UPDATE scheduledwork SET userId = '{0}', fromDate = '{1}', duration = '{2}' WHERE workId = {3};'''.format(userId, fromDate, duration, workId))
    conn.commit()
    cur.close()
    conn.close()

def delete_ScheduledWork(workId):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''delete from scheduledwork where workId = {0} ;'''.format(workId))
    conn.commit()
    cur.close()
    conn.close()