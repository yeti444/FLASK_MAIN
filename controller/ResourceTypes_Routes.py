from flask import Blueprint, jsonify, request
from services.ResourceTypes_Services import get_all_ResourceTypes_service, get_one_ResourceTypes_service, create_ResourceTypes_service, update_ResourceTypes_service, delete_ResourceTypes_service

from utils.utils import role_required

ResourceTypes_bp = Blueprint('ResourceTypes', __name__)

@ResourceTypes_bp.route('/api/ResourceTypes', methods=['GET'])
#@role_required(['Admin', 'User'])
def get_ResourceTypes():
    entries = get_all_ResourceTypes_service()
    ResourceTypes_list = [entry.to_dict() for entry in entries]
    return jsonify({'ResourceTypes': ResourceTypes_list})      

@ResourceTypes_bp.route('/api/ResourceTypes/<int:typeId>', methods=['GET'])
#@role_required(['Admin', 'User'])
def get_one_ResourceTypes(typeId):
    entry = get_one_ResourceTypes_service(typeId)
    return jsonify(entry.to_dict())           

@ResourceTypes_bp.route('/api/ResourceTypes', methods=['POST'])
#@role_required(['Admin'])
def create_ResourceTypes():
    data = request.get_json()
    typeName= data.get('typeName')
    
    if not typeName:
        return jsonify({'error': 'name required'}), 400
    new_entry = create_ResourceTypes_service(typeName)
    return jsonify({'message': 'entry added', 'typeId': new_entry}), 201          

@ResourceTypes_bp.route('/api/ResourceTypes/<int:typeId>', methods=['PUT'])
#@role_required(['Admin'])
def update_ResourceTypes(typeId):
    data = request.get_json()
    typeName= data.get('typeName')
    
    if not typeName:
        return jsonify({'error': 'name required'}), 400
    existing_ResourceType = get_one_ResourceTypes_service(typeId)
    if existing_ResourceType:
        update_ResourceTypes_service(typeId, typeName)
        return jsonify({'message': 'update successful', 'typeId': typeId})
    else:
        return jsonify({'error': 'ResourceType not found'}), 404
    
@ResourceTypes_bp.route('/api/ResourceTypes/<int:typeId>', methods=['DELETE'])
#@role_required(['Admin'])
def delete_ResourceTypes(typeId):
    existing_data = get_one_ResourceTypes_service(typeId)
    if existing_data:
        delete_ResourceTypes_service(typeId)
        return jsonify({'message': 'ResourceTypes deleted successfully', 'typeId': typeId})
    else:
        return jsonify({'error': 'ResourceTypes not found'}), 404