from flask import Blueprint, jsonify, request
from services.UserData_Services import get_all_UserData_service, get_one_UserData_service, create_UserData_service, update_UserData_service, delete_UserData_service, login_UserData_service, update_Password_service
from services.UserRoles_Services import get_one_UserRoles_service

from utils.utils import role_required
from flask_jwt_extended import get_jwt_identity, create_access_token


UserData_bp = Blueprint('UserData', __name__)

def validate_all(data):
    requiredFields = ['email', 'firstName', 'lastName', 'password', 'roleId']
    for field in requiredFields:
        if field not in data:
            return False, f"Missing input data: {field}"
    return True, ""

def validate_some(data):
    requiredFields = ['email', 'firstName', 'lastName', 'roleId']
    for field in requiredFields:
        if field not in data:
            return False, f"Missing input data: {field}"
    return True, ""

def validate_password(data):
    if 'password' not in data:
        return False, "Missing input data: password"
    return True, ""


@UserData_bp.route('/api/UserData', methods=['GET'])
@role_required(['User', 'Admin'])
def get_UserData():
    entries = get_all_UserData_service()
    user_data_dict = {entry.userId: entry.to_dict() for entry in entries}
    return jsonify({'UserData': user_data_dict})

    """
    @UserData_bp.route('/api/UserData', methods=['GET'])
    @role_required(['User', 'Admin'])
    def get_UserData():
        entries = get_all_UserData_service()
        user_data_dict = {entry.userId: entry.to_dict() for entry in entries}
        return jsonify({'UserData': user_data_dict})

    """

@UserData_bp.route('/api/UserData/<int:userId>', methods=['GET'])
@role_required(['User', 'Admin'])
def get_one_UserData(userId):
    entry = get_one_UserData_service(userId)
    return jsonify(entry.to_dict())    

@UserData_bp.route('/api/UserData', methods=['POST'])
@role_required(['Admin'])
def create_UserData():
    data = request.get_json()
    is_valid, error_msg = validate_all(data)
    if not is_valid:
        return jsonify({'error': error_msg}), 400

    try:
        new_entry = create_UserData_service(data['email'], data['firstName'], data['lastName'], data['password'], data['roleId'])
        return jsonify({'message': 'Entry added', 'userId': new_entry}), 201
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': 'Could not create userData', 'details': str(e)}), 500

@UserData_bp.route('/api/UserData/<int:userId>', methods=['PUT'])
@role_required(['Admin', 'User'])
def update_UserData(userId):
    data = request.get_json()
    current_user = get_jwt_identity() 
    curr_userId = current_user['userId']
    curr_role = get_one_UserRoles_service(current_user['roleId']).roleName

    is_valid, error_msg = validate_some(data)
    if not is_valid:
        return jsonify({'error': error_msg}), 400

    existing_user = get_one_UserData_service(userId)
    if not existing_user:
        return jsonify({'error': 'User data not found'}), 404

    try:
        update_UserData_service(data['email'], data['firstName'], data['lastName'], data['roleId'], userId, curr_userId, curr_role)
        new_token = create_access_token(identity=current_user)
        return jsonify({'message': 'Update successful', 'userId': userId, 'email': data['email'], 'token': new_token}), 200
    except ValueError as ve:
        if str(ve) == 'Unauthorized':
            return jsonify({'error': str(ve)}), 403
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': 'Could not update userData', 'details': str(e)}), 500

@UserData_bp.route('/api/changePassword/<int:userId>', methods=['PUT'])
@role_required(['Admin', 'User'])
def update_Password(userId):
    data = request.get_json()
    current_user = get_jwt_identity() 

    is_valid, error_msg = validate_password(data)
    if not is_valid:
        return jsonify({'error': error_msg}), 400

    existing_user = get_one_UserData_service(userId)
    if not existing_user:
        return jsonify({'error': 'User data not found'}), 404

    try:
        update_Password_service(data['password'], userId)
        new_token = create_access_token(identity=current_user)
        return jsonify({'message': 'Update successful', 'userId': userId, 'token': new_token}), 200
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': 'Could not update userData', 'details': str(e)}), 500

@UserData_bp.route('/api/UserData/<int:userId>', methods=['DELETE'])
@role_required(['User', 'Admin'])
def delete_UserData(userId):
    existing_data = get_one_UserData_service(userId)
    if existing_data:
        try:
            delete_UserData_service(userId)
            return jsonify({'message': 'userData deleted successfully', 'userId': userId}), 200
        except Exception as e:
            return jsonify({'error': 'Could not delete userData', 'details': str(e)}), 500
    return jsonify({'error': 'User data not found'}), 404

@UserData_bp.route('/api/login', methods=['POST'])
def login_UserData():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({'error': 'Missing email or password'}), 400
    
    try:
        login_data = login_UserData_service(email, password)
        return jsonify({'message': 'Login successful','token': login_data['token'], 'userId': login_data['userId'], 'email': login_data['email'], 'roleName': login_data['roleName']}), 200
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 401
    except Exception as e:
        return jsonify({'error': 'Unknown', 'details': str(e)}), 500
