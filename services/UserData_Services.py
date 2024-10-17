from repository.UserData_Repository import get_all_UserData, get_one_UserData, create_UserData, update_UserData, delete_UserData, get_one_UserData_email
from utils.utils import hashPassword, checkPassword, is_password_strong, is_valid_email
from flask_jwt_extended import create_access_token


def get_all_UserData_service():
    return get_all_UserData()

def get_one_UserData_service(userId):
    return get_one_UserData(userId)

def create_UserData_service(email, firstName, lastName, password, roleId):
    validate_user_data(email, password)
    return create_UserData(email, firstName, lastName, hashPassword(password), roleId)

def update_UserData_service(email, firstName, lastName, password, roleId, userId):
    validate_user_data(email, password)
    return update_UserData(email, firstName, lastName, hashPassword(password), roleId, userId)

def delete_UserData_service(userId):
    return delete_UserData(userId)

def login_UserData_service(email, password):
    user = get_one_UserData_email(email)
    if user and checkPassword(password, user.password):
        token = create_access_token(identity=user.userId)
        return {
            "token": token,
            "userId": user.userId,
            "email": user.email
        }
    else:
        raise ValueError("Invalid email or password")

def validate_user_data(email, password):
    if not is_valid_email(email):
        raise ValueError('Invalid email format')
    if not is_password_strong(password):
        raise ValueError('Invalid password')

