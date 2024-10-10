from flask import Blueprint, jsonify, request
from services.MaintanedResources_Services import get_all_MaintanedResources_service, get_one_MaintanedResources_service, create_MaintanedResources_service, update_MaintanedResources_service, delete_MaintanedResources_service

MaintanedResources_bp = Blueprint('MaintanedResources', __name__)

@MaintanedResources_bp.route('/api/MaintanedResources', methods=['GET'])
def get_MaintanedResources():
    entries = get_all_MaintanedResources_service()
    MaintanedResources_list = [{'maintId': entry.maintId,'resourceId': entry.resourceId} for entry in entries]
    return jsonify({'MaintanedResources': MaintanedResources_list})          

@MaintanedResources_bp.route('/api/MaintanedResources', methods=['POST'])
def create_MaintanedResources():
    data = request.get_json()
    maintId= data.get('maintId')
    resourceId= data.get('resourceId')
    
    if not maintId or not resourceId:
        return jsonify({'error': 'missing input data'}), 400
    new_entry = create_MaintanedResources_service(maintId, resourceId)
    return jsonify({'message': 'entry added', 'maintId': maintId, 'resourceId': resourceId}), 201    

@MaintanedResources_bp.route('/api/MaintanedResources/<int:maintId>/<int:resourceId>', methods=['PUT'])
def update_MaintanedResources(maintId, resourceId):
    data = request.get_json()
    maintId= data.get('maintId')
    resourceId= data.get('resourceId')
    
    
    if not maintId or not resourceId:
        return jsonify({'error': 'missing input data'}), 400
    existing_MaintanedResources = get_one_MaintanedResources_service(maintId, resourceId)
    if existing_MaintanedResources:
        update_MaintanedResources_service(maintId, resourceId)
        return jsonify({'message': 'update successful', 'maintId': maintId, 'resourceId': resourceId})
    else:
        return jsonify({'error': 'MaintanedResources not found'}), 404

@MaintanedResources_bp.route('/api/MaintanedResources/<int:maintId>/<int:resourceId>', methods=['DELETE'])
def delete_MaintanedResources(maintId, resourceId):
    existing_data = get_one_MaintanedResources_service(maintId, resourceId)
    if existing_data:
        delete_MaintanedResources_service(maintId, resourceId)
        return jsonify({'message': 'MaintanedResources deleted successfully', 'maintId': maintId, 'resourceId': resourceId})
    else:
        return jsonify({'error': 'MaintanedResources not found'}), 404