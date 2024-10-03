from flask import Blueprint, jsonify, request
from services.ResourceTypesServices import get_all_ResourceTypes_service, get_one_ResourceTypes_service, create_ResourceTypes_service, update_ResourceTypes_service, delete_ResourceTypes_service

ResourceTypes_bp = Blueprint('ResourceTypes', __name__)

@ResourceTypes_bp.route('/api/ResourceTypes', methods=['GET'])
def get_ResourceTypes():
    entries = get_all_ResourceTypes_service()
    ResourceTypes_list = [{'typeId': entry.typeId,'typeName':entry.typeName} for entry in entries]
    return jsonify({'ResourceTypes': ResourceTypes_list})                

@ResourceTypes_bp.route('/api/ResourceTypes', methods=['POST'])
def create_ResourceTypes():
    data = request.get_json()
    typeName= data.get('typeName')
    
    if not typeName:
        return jsonify({'error': 'name required'}), 400
    new_entry = create_ResourceTypes_service(typeName)
    return jsonify({'message': 'entry added', 'typeId': new_entry})           

@ResourceTypes_bp.route('/api/ResourceTypes/<int:typeId>', methods=['PUT'])
def update_ResourceTypes(typeId):
    data = request.get_json()
    typeName= data.get('typeName')
    
    if not typeName:
        return jsonify({'error': 'name required'}), 400
    existing_ResourceType = get_one_ResourceTypes_service(typeId)
    if existing_ResourceType:
        update_ResourceTypes_service(typeId, typeName)
        return jsonify({'message': 'update succesfull', 'typeId': typeId})
    else:
        return jsonify({'error': 'ResourceType not found'}), 404
    
@ResourceTypes_bp.route('/api/ResourceTypes/<int:typeId>', methods=['DELETE'])
def delete_ResourceTypes(typeId):
    existing_data = get_one_ResourceTypes_service(typeId)
    if existing_data:
        delete_ResourceTypes_service(typeId)
        return jsonify({'error': 'ResourceTypes deleted succesfully', 'typeId': typeId})
    else:
        return jsonify({'error': 'ResourceTypes not found'}), 404