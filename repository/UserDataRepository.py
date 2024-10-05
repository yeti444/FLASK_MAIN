from db.db_conn import db_conn
from models.UserData import UserData

def get_all_UserData():
    conn = db_conn()
    cur = conn.cursor()
    query = "SELECT * FROM userdata;"
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    conn.close()
    UserData_entries = [UserData(userId = entry[0], email = entry[1], firstName = entry[2], lastName = entry[3], password = entry[4], createDate = entry[5], roleId = entry[6]) for entry in data]
    return UserData_entries

def get_one_UserData(userId):
    conn = db_conn()
    cur = conn.cursor()
    query = "SELECT * FROM userdata WHERE userid = %s;"
    cur.execute(query, (userId,))
    entry = cur.fetchone()
    cur.close()
    conn.close()
    if entry:
        return UserData(userId = entry[0], email = entry[1], firstName = entry[2], lastName = entry[3], password = entry[4], createDate = entry[5], roleId = entry[6])
    else: 
        None
        
def create_UserData(email, firstname, lastname, password, roleId):
    conn = db_conn()
    cur = conn.cursor()
    query = "insert into userdata (email, firstname, lastname, password, roleid) values (%s, %s, %s, %s, %s) returning userId;"
    cur.execute(query, (email, firstname, lastname, password, roleId,)) 
    new_UserData_userId = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return new_UserData_userId

def update_UserData(email, firstname, lastname, password, roleId, userId):
    conn = db_conn()
    cur = conn.cursor()
    query = "UPDATE userdata SET email = %s, firstname = %s, lastname = %s, password = %s, roleid = %s WHERE userid = %s;"
    cur.execute(query, (email, firstname, lastname, password, roleId, userId,))
    conn.commit()
    cur.close()
    conn.close()

def delete_UserData(userid):
    conn = db_conn()
    cur = conn.cursor()
    query = "delete from userdata where userid = {0};"
    cur.execute(query, (userid,))
    conn.commit()
    cur.close()
    conn.close()