from repository.UserData_Repository import get_all_UserData, get_one_UserData, create_UserData, update_UserData, delete_UserData, get_one_UserData_email, update_Password
from repository.UserRoles_Repository import get_one_UserRoles
from utils.utils import hashPassword, checkPassword, validate_user_data, is_valid_email, is_password_strong
from flask_jwt_extended import create_access_token


def get_all_UserData_service():
    return get_all_UserData()

def get_one_UserData_service(userId):
    return get_one_UserData(userId)

def create_UserData_service(email, firstName, lastName, password, roleId):
    validate_user_data(email, password)
    return create_UserData(email, firstName, lastName, hashPassword(password), roleId)

def update_UserData_service(email, firstName, lastName, roleId, userId, curr_userId, curr_role):
    
    if (curr_userId != userId) and (curr_role != 'Admin'):
        raise ValueError('Unauthorized')
    prev_roleId = get_one_UserData(userId).roleId
    
    if (prev_roleId != roleId) and (curr_role != 'Admin'): 
        raise ValueError('Unauthorized')
    
    if not is_valid_email(email):
        raise ValueError('Invalid email format')
    return update_UserData(email, firstName, lastName, roleId, userId)

def update_Password_service(password, userId):
      
    if not is_password_strong(password):
        raise ValueError('Invalid password')
    return update_Password(hashPassword(password), userId)

def delete_UserData_service(userId):
    return delete_UserData(userId)

def login_UserData_service(email, password):
    user = get_one_UserData_email(email)
    if user and checkPassword(password, user.password):
        token = create_access_token(identity={
            'userId': user.userId,
            'roleId': user.roleId
        })
        return {
            "token": token,
            "userId": user.userId,
            "email": user.email,
            "roleName": get_one_UserRoles(user.roleId).roleName
        }
    else:
        raise ValueError("Invalid email or password")




