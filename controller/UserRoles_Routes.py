from flask import Blueprint, jsonify, request
from services.UserRoles_Services import get_all_UserRoles_service, get_one_UserRoles_service, create_UserRoles_service, update_UserRoles_service, delete_UserRoles_service

from utils.utils import role_required

UserRoles_bp = Blueprint('UserRoles', __name__)

@UserRoles_bp.route('/api/UserRoles', methods=['GET'])
@role_required(['Admin', 'User'])
def get_UserRoles():
    entries = get_all_UserRoles_service()
    UserRoles_list = [entry.to_dict() for entry in entries]
    return jsonify({'UserRoles': UserRoles_list})   

@UserRoles_bp.route('/api/UserRoles/<int:roleId>', methods=['GET'])
@role_required(['Admin', 'User'])
def get_one_UserRoles(roleId):
    entry = get_one_UserRoles_service(roleId)
    return jsonify(entry.to_dict())               

@UserRoles_bp.route('/api/UserRoles', methods=['POST'])
@role_required(['Mistake']) #2db jogosultsági szint van csak, nem kell módosítani TODO: dinamikus jogosultságok
def create_UserRoles():
    data = request.get_json()
    roleName= data.get('roleName')
    
    if not roleName:
        return jsonify({'error': 'name required'}), 400
    new_entry = create_UserRoles_service(roleName)
    return jsonify({'message': 'entry added', 'roleId': new_entry}), 201           

@UserRoles_bp.route('/api/UserRoles/<int:roleId>', methods=['PUT'])
@role_required(['Mistake']) #2db jogosultsági szint van csak, nem kell módosítani TODO: dinamikus jogosultságok
def update_UserRoles(roleId):
    data = request.get_json()
    roleName= data.get('roleName')
    
    if not roleName:
        return jsonify({'error': 'name required'}), 400
    existing_UserRoles = get_one_UserRoles_service(roleId)
    if existing_UserRoles:
        update_UserRoles_service(roleId, roleName)
        return jsonify({'message': 'update successful', 'roleId': roleId})
    else:
        return jsonify({'error': 'UserRoles not found'}), 404
    
@UserRoles_bp.route('/api/UserRoles/<int:roleId>', methods=['DELETE'])
@role_required(['Mistake']) #2db jogosultsági szint van csak, nem kell módosítani TODO: dinamikus jogosultságok
def delete_UserRoles(roleId):
    existing_data = get_one_UserRoles_service(roleId)
    if existing_data:
        delete_UserRoles_service(roleId)
        return jsonify({'message': 'UserRoles deleted successfully', 'roleId': roleId})
    else:
        return jsonify({'error': 'UserRoles not found'}), 404