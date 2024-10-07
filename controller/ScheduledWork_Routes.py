from flask import Blueprint, jsonify, request
from services.ScheduledWork_Services import get_all_ScheduledWork_service, get_one_ScheduledWork_service, create_ScheduledWork_service, update_ScheduledWork_service, delete_ScheduledWork_service
ScheduledWork_bp = Blueprint('ScheduledWork', __name__)

@ScheduledWork_bp.route('/api/ScheduledWork', methods=['GET'])
def get_ScheduledWork():
    entries = get_all_ScheduledWork_service()
    ScheduledWork_list = [{'workId': entry.workId,'userId': entry.userId,'fromDate': entry.fromDate,'duration': entry.duration,'createDate': entry.createDate} for entry in entries]
    return jsonify({'ScheduledWork': ScheduledWork_list})          

@ScheduledWork_bp.route('/api/ScheduledWork', methods=['POST'])
def create_ScheduledWork():
    data = request.get_json()
    userId= data.get('userId')
    fromDate= data.get('fromDate')
    duration= data.get('duration')
    
    if not userId or not fromDate or not duration:
        return jsonify({'error': 'missing input data'}), 400
    new_entry = create_ScheduledWork_service(userId, fromDate, duration)
    return jsonify({'message': 'entry added', 'workId': new_entry})    

@ScheduledWork_bp.route('/api/ScheduledWork/<int:workId>', methods=['PUT'])
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
        return jsonify({'message': 'update succesfull', 'workId': workId})
    else:
        return jsonify({'error': 'ScheduledWork not found'}), 404

@ScheduledWork_bp.route('/api/ScheduledWork/<int:workId>', methods=['DELETE'])
def delete_ScheduledWork(workId):
    existing_data = get_one_ScheduledWork_service(workId)
    if existing_data:
        delete_ScheduledWork_service(workId)
        return jsonify({'error': 'ScheduledWork deleted succesfully', 'workId': workId})
    else:
        return jsonify({'error': 'ScheduledWork not found'}), 404