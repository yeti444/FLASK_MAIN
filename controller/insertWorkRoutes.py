from flask import Blueprint, jsonify, request
from services.insertWorkServices import insertNewScheduledWork_service

insertWork_bp = Blueprint('inserWork', __name__)

@insertWork_bp.route('/api/insertWork', methods=['POST'])
def insertWork():
    data = request.get_json()
    resourceId= data.get('resourceId')
    userId= data.get('userId')
    fromDate= data.get('fromDate')
    duration= data.get('duration')
    
    if not resourceId or not userId or not fromDate or not duration:
        return jsonify({'error': 'missing input data'}), 400
    new_entry = insertNewScheduledWork_service(resourceId, userId, fromDate, duration)
    return jsonify({'message': 'entry added', 'workId': new_entry, 'resourceId': resourceId})  

