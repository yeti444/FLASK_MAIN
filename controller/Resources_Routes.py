from flask import Blueprint, jsonify, request
from services.Resources_Services import get_all_Resources_Service, get_one_Resources_service, create_Resources_service, update_Resources_service, delete_Resources_service

Resources_bp = Blueprint('Resources', __name__)

@Resources_bp.route('/api/Resources', methods=['GET'])
def get_Resources():
    entries = get_all_Resources_Service()
    Resources_list = [{'resourceId': entry.resourceId,'name':entry.name,'typeId':entry.typeId,'info':entry.info,'createDate':entry.createDate} for entry in entries]
    return jsonify({'Resources': Resources_list})                

@Resources_bp.route('/api/Resources', methods=['POST'])
def create_Resources():
    data = request.get_json()
    name= data.get('name')
    typeId= data.get('typeId')
    info= data.get('info')
    
    if not name or not typeId or not info:
        return jsonify({'error': 'missing input data'}), 400
    new_entry = create_Resources_service(name, typeId, info)
    return jsonify({'message': 'entry added', 'resourceId': new_entry}), 201         

@Resources_bp.route('/api/Resources/<int:resourceId>', methods=['PUT'])
def update_Resources(resourceId):
    data = request.get_json()
    name= data.get('name')
    typeId= data.get('typeId')
    info= data.get('info')
    
    if not name or not typeId or not info:
        return jsonify({'error': 'missing input data'}), 400
    existing_Resources = get_one_Resources_service(resourceId)
    if existing_Resources:
        update_Resources_service(resourceId, name, typeId, info)
        return jsonify({'message': 'update successful', 'resourceId': resourceId})
    else:
        return jsonify({'error': 'Resource not found'}), 404
    
@Resources_bp.route('/api/Resources/<int:resourceId>', methods=['DELETE'])
def delete_Resources(resourceId):
    existing_data = get_one_Resources_service(resourceId)
    if existing_data:
        delete_Resources_service(resourceId)
        return jsonify({'message': 'Resources deleted successfully', 'resourceId': resourceId})
    else:
        return jsonify({'error': 'Resources not found'}), 404