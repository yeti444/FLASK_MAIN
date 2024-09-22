from flask import Blueprint, jsonify, request
from services.ScheduledMaintenanceServices import get_all_ScheduledMaintenance_service, get_one_ScheduledMaintenance_service, create_ScheduledMaintenance_service, update_ScheduledMaintenance_service, delete_ScheduledMaintenance_service
ScheduledMaintenance_bp = Blueprint('ScheduledMaintenance', __name__)

@ScheduledMaintenance_bp.route('/api/ScheduledMaintenance', methods=['GET'])
def get_ScheduledMaintenance():
    entries = get_all_ScheduledMaintenance_service()
    ScheduledMaintenance_list = [{'maintId': entry.maintId,'userId': entry.userId,'fromDate': entry.fromDate,'duration': entry.duration,'createDate': entry.createDate} for entry in entries]
    return jsonify({'ScheduledMaintenance': ScheduledMaintenance_list})          

@ScheduledMaintenance_bp.route('/api/ScheduledMaintenance', methods=['POST'])
def create_ScheduledMaintenance():
    data = request.get_json()
    userId= data.get('userId')
    fromDate= data.get('fromDate')
    duration= data.get('duration')
    
    if not userId or not fromDate or not duration:
        return jsonify({'error': 'missing input data'}), 400
    new_entry = create_ScheduledMaintenance_service(userId, fromDate, duration)
    return jsonify({'message': 'entry added', 'maintId': new_entry})    

@ScheduledMaintenance_bp.route('/api/ScheduledMaintenance/<int:maintId>', methods=['PUT'])
def update_ScheduledMaintenance(maintId):
    data = request.get_json()
    userId= data.get('userId')
    fromDate= data.get('fromDate')
    duration= data.get('duration')
    
    if not userId or not fromDate or not duration:
        return jsonify({'error': 'missing input data'}), 400
    existing_userId = get_one_ScheduledMaintenance_service(maintId)
    if existing_userId:
        update_ScheduledMaintenance_service(maintId, userId, fromDate, duration)
        return jsonify({'message': 'update succesfull', 'maintId': maintId})
    else:
        return jsonify({'error': 'ScheduledMaintenance not found'}), 404

@ScheduledMaintenance_bp.route('/api/ScheduledMaintenance/<int:maintId>', methods=['DELETE'])
def delete_ScheduledMaintenance(maintId):
    existing_data = get_one_ScheduledMaintenance_service(maintId)
    if existing_data:
        delete_ScheduledMaintenance_service(maintId)
        return jsonify({'error': 'ScheduledMaintenance deleted succesfully', 'maintId': maintId})
    else:
        return jsonify({'error': 'ScheduledMaintenance not found'}), 404