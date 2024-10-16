from repository.UserData_Repository import get_all_UserData, get_one_UserData, create_UserData, update_UserData, delete_UserData
from utils.utils import hashPassword, checkPassword, is_password_strong, is_valid_email

def get_all_UserData_service():
    return get_all_UserData()

def get_one_UserData_service(userId):
    return get_one_UserData(userId)

def create_UserData_service(email, firstName, lastName, password, roleId):
    if not is_valid_email(email):
        raise ValueError('invalid email format')
    
    if not is_password_strong(password):
        raise ValueError('invalid password')

    return create_UserData(email, firstName, lastName, hashPassword(password), roleId)



def update_UserData_service(email, firstName, lastName, password, roleId, userId):
    if not is_valid_email(email):
        raise ValueError('invalid email format')
    if not is_password_strong(password):
        raise ValueError('invalid password')
    
    return update_UserData(email, firstName, lastName, hashPassword(password), roleId, userId)

def delete_UserData_service(userid):
    return delete_UserData(userid)
