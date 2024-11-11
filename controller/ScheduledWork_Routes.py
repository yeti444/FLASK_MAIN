from flask import Blueprint, jsonify, request
from services.ScheduledWork_Services import get_all_ScheduledWork_service, get_one_ScheduledWork_service, create_ScheduledWork_service, update_ScheduledWork_service, delete_ScheduledWork_service

from utils.utils import role_required

ScheduledWork_bp = Blueprint('ScheduledWork', __name__)

@ScheduledWork_bp.route('/api/ScheduledWork', methods=['GET'])
#@role_required(['Admin', 'User'])
def get_ScheduledWork():
    entries = get_all_ScheduledWork_service()
    ScheduledWork_list = [entry.to_dict() for entry in entries]
    return jsonify({'ScheduledWork': ScheduledWork_list})          

@ScheduledWork_bp.route('/api/ScheduledWork/<int:workId>', methods=['GET'])
#@role_required(['Admin', 'User'])
def get_one_ScheduledWork(workId):
    entry = get_one_ScheduledWork_service(workId)
    return jsonify(entry.to_dict())    

@ScheduledWork_bp.route('/api/ScheduledWork', methods=['POST'])
#@role_required(['Admin', 'User'])
def create_ScheduledWork():
    data = request.get_json()
    userId= data.get('userId')
    fromDate= data.get('fromDate')
    duration= data.get('duration')
    
    if not userId or not fromDate or not duration:
        return jsonify({'error': 'missing input data'}), 400
    new_entry = create_ScheduledWork_service(userId, fromDate, duration)
    return jsonify({'message': 'entry added', 'workId': new_entry}), 201 

@ScheduledWork_bp.route('/api/ScheduledWork/<int:workId>', methods=['PUT'])
#@role_required(['Admin', 'User'])
def update_ScheduledWork(workId):
    data = request.get_json()
    userId= data.get('userId')
    fromDate= data.get('fromDate')
    duration= data.get('duration')
    
    if not userId or not fromDate or not duration:
        return jsonify({'error': 'missing input data'}), 400
    existing_userId = get_one_ScheduledWork_service(workId)
    if existing_userId:
        update_ScheduledWork_service(workId, userId, fromDate, duration)
        return jsonify({'message': 'update successful', 'workId': workId})
    else:
        return jsonify({'error': 'ScheduledWork not found'}), 404

@ScheduledWork_bp.route('/api/ScheduledWork/<int:workId>', methods=['DELETE'])
#@role_required(['Admin', 'User'])
def delete_ScheduledWork(workId):
    existing_data = get_one_ScheduledWork_service(workId)
    if existing_data:
        delete_ScheduledWork_service(workId)
        return jsonify({'message': 'ScheduledWork deleted successfully', 'workId': workId})
    else:
        return jsonify({'error': 'ScheduledWork not found'}), 404