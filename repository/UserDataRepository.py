import psycopg2
from models.UserData import UserData

def db_conn():
    return psycopg2.connect(database="resourceManagement", host="localhost", user="", password="lenin17", port="5432")

def get_all_UserData():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM userdata''')
    data = cur.fetchall()
    cur.close()
    conn.close()
    UserData_entries = [UserData(userId = entry[0], email = entry[1], firstName = entry[2], lastName = entry[3], password = entry[4], createDate = entry[5], roleId = entry[6]) for entry in data]
    return UserData_entries

def get_one_UserData(userId):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM userdata WHERE userid = {0}'''.format(userId))
    UserData_entry = cur.fetchone()
    cur.close()
    conn.close()
    if UserData_entry:
        return UserData(userId = UserData_entry[0], email = UserData_entry[1], firstName = UserData_entry[2], lastName = UserData_entry[3], password = UserData_entry[4], createDate = UserData_entry[5], roleId = UserData_entry[6])
    else: 
        None
        
def create_UserData(email, firstname, lastname, password, roleId):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''insert into userdata (email, firstname, lastname, password, roleid) values ('{0}', '{1}', '{2}', '{3}', {4}) returning userId;'''.format(email, firstname, lastname, password, roleId))
    new_UserData_userId = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return new_UserData_userId

def update_UserData(email, firstname, lastname, password, roleId, userId):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''UPDATE userdata SET email = '{0}', firstname = '{1}', lastname = '{2}', password = '{3}', roleid = '{4}' WHERE userid = '{5}' ;'''.format(email, firstname, lastname, password, roleId, userId))
    conn.commit()
    cur.close()
    conn.close()

def delete_UserData(userid):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''delete from userdata where userid = {0} ;'''.format(userid))
    conn.commit()
    cur.close()
    conn.close()