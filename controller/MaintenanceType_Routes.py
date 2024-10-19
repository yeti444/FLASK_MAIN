from flask import Blueprint, jsonify, request
from services.MaintenanceType_Services import get_all_MaintenanceType_service, get_one_MaintenanceType_service, create_MaintenanceType_service, update_MaintenanceType_service, delete_MaintenanceType_service
from utils.utils import role_required


MaintenanceType_bp = Blueprint('MaintenanceType', __name__)

@MaintenanceType_bp.route('/api/MaintenanceType', methods=['GET'])
@role_required(['Admin', 'User'])
def get_MaintenanceType():
    entries = get_all_MaintenanceType_service()
    MaintenanceType_list = [entry.to_dict() for entry in entries]
    return jsonify({'MaintenanceType': MaintenanceType_list})  

@MaintenanceType_bp.route('/api/MaintenanceType', methods=['POST'])
@role_required(['Admin'])
def create_MaintenanceType():
    data = request.get_json()
    typeName= data.get('typeName')
    
    if not typeName:
        return jsonify({'error': 'name required'}), 400
    new_entry = create_MaintenanceType_service(typeName)
    return jsonify({'message': 'entry added', 'maintenanceTypeId': new_entry}), 201           

@MaintenanceType_bp.route('/api/MaintenanceType/<int:maintenanceTypeId>', methods=['PUT'])
@role_required(['Admin'])
def update_MaintenanceType(maintenanceTypeId):
    data = request.get_json()
    typeName= data.get('typeName')
    
    if not typeName:
        return jsonify({'error': 'name required'}), 400
    existing_maintenanceType = get_one_MaintenanceType_service(maintenanceTypeId)
    if existing_maintenanceType:
        update_MaintenanceType_service(maintenanceTypeId, typeName)
        return jsonify({'message': 'update successful', 'maintenanceTypeId': maintenanceTypeId})
    else:
        return jsonify({'error': 'maintenanceType not found'}), 404
    
@MaintenanceType_bp.route('/api/MaintenanceType/<int:maintenanceTypeId>', methods=['DELETE'])
@role_required(['Admin'])
def delete_MaintenanceType(maintenanceTypeId):
    existing_data = get_one_MaintenanceType_service(maintenanceTypeId)
    if existing_data:
        delete_MaintenanceType_service(maintenanceTypeId)
        return jsonify({'message': 'maintenanceType deleted successfully', 'maintenanceTypeId': maintenanceTypeId})
    else:
        return jsonify({'error': 'maintenanceType not found'}), 404
