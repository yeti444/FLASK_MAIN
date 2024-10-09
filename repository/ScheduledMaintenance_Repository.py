from db.db_conn import db_conn
from models.ScheduledMaintenance import ScheduledMaintenance


def get_all_ScheduledMaintenance():
    conn = db_conn()
    cur = conn.cursor()
    query = "SELECT * FROM scheduledmaintenance;"
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    conn.close()
    ScheduledWork_entries = [ScheduledMaintenance(maintId = entry[0], userId = entry[1], fromDate = entry[2], duration = entry[3], createDate = entry[4], description=entry[5], maintenancetypeid=entry[6]) for entry in data]
    return ScheduledWork_entries

def get_one_ScheduledMaintenance(maintId):
    conn = db_conn()
    cur = conn.cursor()
    query = "SELECT * FROM scheduledmaintenance WHERE maintId = %s;"
    cur.execute(query, (maintId,))
    entry = cur.fetchone()
    cur.close()
    conn.close()
    if ScheduledMaintenance:
        return ScheduledMaintenance(maintId = entry[0], userId = entry[1], fromDate = entry[2], duration = entry[3], createDate = entry[4], description=entry[5], maintenancetypeid=entry[6])
    else: 
        None

def create_ScheduledMaintenance(userId, fromDate, duration, description, maintenancetypeid):
    conn = db_conn()
    cur = conn.cursor()
    query = "insert into scheduledmaintenance (userId, fromDate, duration, description, maintenancetypeid) values (%s, %s, %s, %s, %s) returning maintId;"
    cur.execute(query, (userId, fromDate, duration, description, maintenancetypeid,))
    new_ScheduledMaintenance_maintId = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return new_ScheduledMaintenance_maintId

def update_ScheduledMaintenance(maintId, userId, fromDate, duration, description, maintenancetypeid):
    conn = db_conn()
    cur = conn.cursor()
    query = "UPDATE scheduledmaintenance SET userId = %s, fromDate = %s, duration = %s, description = %s, maintenancetypeid = %s WHERE maintId = %s;"
    cur.execute(query, (userId, fromDate, duration, description, maintenancetypeid, maintId))
    conn.commit()
    cur.close()
    conn.close()

def delete_ScheduledMaintenance(maintId):
    conn = db_conn()
    cur = conn.cursor()
    query = "delete from scheduledmaintenance where maintId = %s;"
    cur.execute(query, (maintId,))
    conn.commit()
    cur.close()
    conn.close()