from db.db_conn import db_conn
from models.UserRoles import UserRoles

def get_all_UserRoles():
    conn = db_conn()
    cur = conn.cursor()
    query = "SELECT * FROM userroles;"
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    conn.close()
    UserRoles_entries = [UserRoles(roleId=entry[0], roleName=entry[1]) for entry in data]
    return UserRoles_entries

def get_one_UserRoles(roleId):
    conn = db_conn()
    cur = conn.cursor()
    query = "SELECT * FROM userroles WHERE roleId = %s;"
    cur.execute(query, (roleId,))
    entry = cur.fetchone()
    cur.close()
    conn.close()
    if entry:
        return UserRoles(roleId=entry[0], roleName=entry[1])
    else: 
        return None

def create_UserRoles(roleName):
    conn = db_conn()
    cur = conn.cursor()
    query = "insert into userroles (roleName) values (%s) returning roleId;"
    cur.execute(query, (roleName,))
    new_UserRoles_roleId = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return new_UserRoles_roleId

def update_UserRoles(roleId, roleName):
    conn = db_conn()
    cur = conn.cursor()
    query = "UPDATE userroles SET roleName = %s WHERE roleId = %s;"
    cur.execute(query, (roleName, roleId,))
    conn.commit()
    cur.close()
    conn.close()
    
def delete_UserRoles(roleId):
    conn = db_conn()
    cur = conn.cursor()
    query = "delete from userroles where roleId = %s;"
    cur.execute(query, (roleId,))
    conn.commit()
    cur.close()
    conn.close()