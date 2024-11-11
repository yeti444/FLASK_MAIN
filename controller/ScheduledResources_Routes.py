from flask import Blueprint, jsonify, request
from services.ScheduledResources_Services import get_all_ScheduledResources_service, get_one_ScheduledResources_service, create_ScheduledResources_service, update_ScheduledResources_service, delete_ScheduledResources_service

from utils.utils import role_required

ScheduledResources_bp = Blueprint('ScheduledResources', __name__)

@ScheduledResources_bp.route('/api/ScheduledResources', methods=['GET'])
#@role_required(['Admin', 'User'])
def get_ScheduledResources():
    entries = get_all_ScheduledResources_service()
    ScheduledResources_list = [entry.to_dict() for entry in entries]
    return jsonify({'ScheduledResources': ScheduledResources_list})          

@ScheduledResources_bp.route('/api/ScheduledResources/<int:workId>/<int:resourceId>', methods=['GET'])
#@role_required(['Admin', 'User'])
def get_one_ScheduledResources(workId, resourceId):
    entry = get_one_ScheduledResources_service(workId, resourceId)
    return jsonify(entry.to_dict())    

@ScheduledResources_bp.route('/api/ScheduledResources', methods=['POST'])
#@role_required(['Admin', 'User'])
def create_ScheduledResources():
    data = request.get_json()
    workId= data.get('workId')
    resourceId= data.get('resourceId')
    
    if not workId or not resourceId:
        return jsonify({'error': 'missing input data'}), 400
    new_entry = create_ScheduledResources_service(workId, resourceId)
    return jsonify({'message': 'entry added', 'workId': workId, 'resourceId': resourceId}), 201    

@ScheduledResources_bp.route('/api/ScheduledResources/<int:workId>/<int:resourceId>', methods=['PUT'])
#@role_required(['Admin', 'User'])
def update_ScheduledResources(workId, resourceId):
    data = request.get_json()
    new_workId= data.get('workId')
    new_resourceId= data.get('resourceId')

    if not workId or not resourceId or not new_workId or not new_resourceId:
        return jsonify({'error': 'missing input data'}), 400
    existing_ScheduledResources = get_one_ScheduledResources_service(workId, resourceId)
    if existing_ScheduledResources:
        update_ScheduledResources_service(new_workId, new_resourceId, workId, resourceId)
        return jsonify({'message': 'update successful', 'workId': workId, 'resourceId': resourceId})
    else:
        return jsonify({'error': 'ScheduledResources not found'}), 404

@ScheduledResources_bp.route('/api/ScheduledResources/<int:workId>/<int:resourceId>', methods=['DELETE'])
#@role_required(['Admin', 'User'])
def delete_ScheduledResources(workId, resourceId):
    existing_data = get_one_ScheduledResources_service(workId, resourceId)
    if existing_data:
        delete_ScheduledResources_service(workId, resourceId)
        return jsonify({'message': 'ScheduledResources deleted successfully', 'workId': workId, 'resourceId': resourceId})
    else:
        return jsonify({'error': 'ScheduledResources not found'}), 404