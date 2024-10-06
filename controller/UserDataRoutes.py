from flask import Blueprint, jsonify, request
from services.UserDataServices import get_all_UserData_service, get_one_UserData_service, create_UserData_service, update_UserData_service, delete_UserData_service



UserData_bp = Blueprint('UserData', __name__)

@UserData_bp.route('/api/UserData', methods=['GET'])
def get_UserData():
    entries = get_all_UserData_service()
    UserData_list = [{'userId': entry.userId,'email': entry.email,'firstName': entry.firstName,'lastName': entry.lastName,'password': entry.password,'createDate': entry.createDate,'roleId': entry.roleId} for entry in entries]
    return jsonify({'UserData': UserData_list})   


@UserData_bp.route('/api/UserData', methods=['POST'])
def create_UserData():
    data = request.get_json()
    email= data.get('email')
    firstName= data.get('firstName')
    lastName= data.get('lastName')
    password= data.get('password')
    roleId= data.get('roleId')
    
    if not email or not firstName or not lastName or not password or not roleId:
        return jsonify({'error': 'missing input data'}), 400
    new_entry = create_UserData_service(email, firstName, lastName, password, roleId)
    return jsonify({'message': 'entry added', 'userId': new_entry})    

@UserData_bp.route('/api/UserData/<int:userId>', methods=['PUT'])
def update_UserData(userId):
    data = request.get_json()
    email= data.get('email')
    firstName= data.get('firstName')
    lastName= data.get('lastName')
    password= data.get('password')
    roleId= data.get('roleId')
    
    if not email or not firstName or not lastName or not password or not roleId:
        return jsonify({'error': 'missing input data'}), 400
    existing_userId = get_one_UserData_service(userId)
    if existing_userId:
        update_UserData_service(email, firstName, lastName, password, roleId, userId)
        return jsonify({'message': 'update succesfull', 'userId': userId})
    else:
        return jsonify({'error': 'userData not found'}), 404

@UserData_bp.route('/api/UserData/<int:userId>', methods=['DELETE'])
def delete_UserData(userId):
    existing_data = get_one_UserData_service(userId)
    if existing_data:
        delete_UserData_service(userId)
        return jsonify({'error': 'userData deleted succesfully', 'userId': userId})
    else:
        return jsonify({'error': 'userData not found'}), 404