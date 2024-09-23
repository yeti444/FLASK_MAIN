import psycopg2
from models.UserRoles import UserRoles

def db_conn():
    return psycopg2.connect(database="resourceManagement", host="localhost", user="", password="lenin17", port="5432")

def get_all_UserRoles():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM userroles''')
    data = cur.fetchall()
    cur.close()
    conn.close()
    UserRoles_entries = [UserRoles(roleId=entry[0], roleName=entry[1]) for entry in data]
    return UserRoles_entries

def get_one_UserRoles(roleId):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM userroles WHERE roleId = {0}'''.format(roleId))
    UserRoles_entry = cur.fetchone()
    cur.close()
    conn.close()
    if UserRoles_entry:
        return UserRoles(roleId=UserRoles_entry[0], roleName=UserRoles_entry[1])
    else: 
        None

def create_UserRoles(roleName):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''insert into userroles (roleName) values ('{0}') returning roleId;'''.format(roleName))
    new_UserRoles_roleId = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return new_UserRoles_roleId

def update_UserRoles(roleId, roleName):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''UPDATE userroles SET roleName = '{0}' WHERE roleId = {1} ;'''.format(roleName, roleId))
    conn.commit()
    cur.close()
    conn.close()
    
def delete_UserRoles(roleId):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''delete from userroles where roleId = {0} ;'''.format(roleId))
    conn.commit()
    cur.close()
    conn.close()