import psycopg2
from models.ScheduledMaintenance import ScheduledMaintenance

def db_conn():
    return psycopg2.connect(database="resourceManagement", host="localhost", user="", password="lenin17", port="5432")

def get_all_ScheduledMaintenance():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM scheduledmaintenance''')
    data = cur.fetchall()
    cur.close()
    conn.close()
    ScheduledWork_entries = [ScheduledMaintenance(maintId = entry[0], userId = entry[1], fromDate = entry[2], duration = entry[3], createDate = entry[4], description=entry[5], maintenancetypeid=entry[6]) for entry in data]
    return ScheduledWork_entries

def get_one_ScheduledMaintenance(maintId):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM scheduledmaintenance WHERE maintId = {0}'''.format(maintId))
    ScheduledMaintenance_entry = cur.fetchone()
    cur.close()
    conn.close()
    if ScheduledMaintenance:
        return ScheduledMaintenance(maintId = ScheduledMaintenance_entry[0], userId = ScheduledMaintenance_entry[1], fromDate = ScheduledMaintenance_entry[2], duration = ScheduledMaintenance_entry[3], createDate = ScheduledMaintenance_entry[4], description=ScheduledMaintenance_entry[5], maintenancetypeid=ScheduledMaintenance_entry[6])
    else: 
        None

def create_ScheduledMaintenance(userId, fromDate, duration, description, maintenancetypeid):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''insert into scheduledmaintenance (userId, fromDate, duration, description, maintenancetypeid) values ('{0}', '{1}', '{2}', '{3}', '{4}') returning maintId;'''.format(userId, fromDate, duration, description, maintenancetypeid))
    new_ScheduledMaintenance_maintId = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return new_ScheduledMaintenance_maintId

def update_ScheduledMaintenance(maintId, userId, fromDate, duration, description, maintenancetypeid):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''UPDATE scheduledmaintenance SET userId = '{0}', fromDate = '{1}', duration = '{2}', description = '{3}', maintenancetypeid = '{4}' WHERE maintId = {3};'''.format(userId, fromDate, duration, maintId, description, maintenancetypeid))
    conn.commit()
    cur.close()
    conn.close()

def delete_ScheduledMaintenance(maintId):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''delete from scheduledmaintenance where maintId = {0} ;'''.format(maintId))
    conn.commit()
    cur.close()
    conn.close()