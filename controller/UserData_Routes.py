from flask import Blueprint, jsonify, request
from services.UserData_Services import get_all_UserData_service, get_one_UserData_service, create_UserData_service, update_UserData_service, delete_UserData_service, login_UserData_service

from flask_jwt_extended import jwt_required


UserData_bp = Blueprint('UserData', __name__)

def validate_user_data(data):
    required_fields = ['email', 'firstName', 'lastName', 'password', 'roleId']
    for field in required_fields:
        if field not in data:
            return False, f"Missing input data: {field}"
    return True, ""

@UserData_bp.route('/api/UserData', methods=['GET'])
def get_UserData():
    entries = get_all_UserData_service()
    return jsonify({'UserData': [entry.to_dict() for entry in entries]})

@UserData_bp.route('/api/UserData', methods=['POST'])
def create_UserData():
    data = request.get_json()
    is_valid, error_msg = validate_user_data(data)
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
#@jwt_required()
def update_UserData(userId):
    data = request.get_json()
    is_valid, error_msg = validate_user_data(data)
    if not is_valid:
        return jsonify({'error': error_msg}), 400

    existing_user = get_one_UserData_service(userId)
    if not existing_user:
        return jsonify({'error': 'User data not found'}), 404

    try:
        update_UserData_service(data['email'], data['firstName'], data['lastName'], data['password'], data['roleId'], userId)
        return jsonify({'message': 'Update successful', 'userId': userId}), 200
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': 'Could not update userData', 'details': str(e)}), 500

@UserData_bp.route('/api/UserData/<int:userId>', methods=['DELETE'])
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
        return jsonify({'message': 'Login successful','token': login_data['token'], 'userId': login_data['userId'], 'email': login_data['email']}), 200
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 401
    except Exception as e:
        return jsonify({'error': 'Unknown', 'details': str(e)}), 500
