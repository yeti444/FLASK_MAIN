from db.db_conn import db_conn
from models.MaintenanceType import MaintenanceType

def get_all_MaintenanceType():
    conn = db_conn()
    cur = conn.cursor()
    query = "SELECT * FROM maintenancetype;"
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    conn.close()
    MaintenanceType_entries = [MaintenanceType(maintenanceTypeId=entry[0], typeName=entry[1]) for entry in data]
    return MaintenanceType_entries

def get_one_MaintenanceType(maintenanceTypeId):
    conn = db_conn()
    cur = conn.cursor()
    query = "SELECT * FROM maintenancetype WHERE maintenanceTypeId = %s;"
    cur.execute(query, (maintenanceTypeId,))
    entry = cur.fetchone()
    cur.close()
    conn.close()
    if entry:
        return MaintenanceType(maintenanceTypeId=entry[0], typeName=entry[1])
    else: 
        None

def create_MaintenanceType(typeName):
    conn = db_conn()
    cur = conn.cursor()
    query = "insert into maintenancetype (typeName) values (%s) returning maintenanceTypeId;"
    cur.execute(query, (typeName,))
    new_MaintenanceType_maintenanceTypeId = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return new_MaintenanceType_maintenanceTypeId

def update_MaintenanceType(maintenanceTypeId, typeName):
    conn = db_conn()
    cur = conn.cursor()
    query = "UPDATE maintenancetype SET typeName = %s WHERE maintenanceTypeId = %s;"
    cur.execute(query, (typeName, maintenanceTypeId,))
    conn.commit()
    cur.close()
    conn.close()
    
def delete_MaintenanceType(maintenanceTypeId):
    conn = db_conn()
    cur = conn.cursor()
    query = "delete from maintenancetype where maintenanceTypeId = %s;"
    cur.execute(query, (maintenanceTypeId,))
    conn.commit()
    cur.close()
    conn.close()