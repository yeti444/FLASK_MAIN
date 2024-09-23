from flask import Blueprint, jsonify, request
from services.ScheduledResourcesServices import get_all_ScheduledResources_service, get_one_ScheduledResources_service, create_ScheduledResources_service, update_ScheduledResources_service, delete_ScheduledResources_service

ScheduledResources_bp = Blueprint('ScheduledResources', __name__)

@ScheduledResources_bp.route('/api/ScheduledResources', methods=['GET'])
def get_ScheduledResources():
    entries = get_all_ScheduledResources_service()
    ScheduledResources_list = [{'workId': entry.workId,'resourceId': entry.resourceId} for entry in entries]
    return jsonify({'ScheduledResources': ScheduledResources_list})          

@ScheduledResources_bp.route('/api/ScheduledResources', methods=['POST'])
def create_ScheduledResources():
    data = request.get_json()
    workId= data.get('workId')
    resourceId= data.get('resourceId')
    
    if not workId or not resourceId:
        return jsonify({'error': 'missing input data'}), 400
    new_entry = create_ScheduledResources_service(workId, resourceId)
    return jsonify({'message': 'entry added', 'workId': workId, 'resourceId': resourceId})    

@ScheduledResources_bp.route('/api/ScheduledResources/<int:workId>&<int:resourceId>', methods=['PUT'])
def update_ScheduledResources(workId, resourceId):
    data = request.get_json()
    workId= data.get('workId')
    resourceId= data.get('resourceId')
    
    
    if not workId or not resourceId:
        return jsonify({'error': 'missing input data'}), 400
    existing_ScheduledResources = get_one_ScheduledResources_service(workId, resourceId)
    if existing_ScheduledResources:
        update_ScheduledResources_service(workId, resourceId)
        return jsonify({'message': 'update succesfull', 'workId': workId, 'resourceId': resourceId})
    else:
        return jsonify({'error': 'ScheduledResources not found'}), 404

@ScheduledResources_bp.route('/api/ScheduledResources/<int:workId>&<int:resourceId>', methods=['DELETE'])
def delete_ScheduledResources(workId, resourceId):
    existing_data = get_one_ScheduledResources_service(workId, resourceId)
    if existing_data:
        delete_ScheduledResources_service(workId, resourceId)
        return jsonify({'error': 'ScheduledResources deleted succesfully', 'workId': workId, 'resourceId': resourceId})
    else:
        return jsonify({'error': 'ScheduledResources not found'}), 404