from flask import Blueprint, jsonify, request
from services.Insert_Services import insertNewScheduledWork_service, insertNewMaintenance_service

from utils.utils import role_required

insertWork_bp = Blueprint('inserWork', __name__)
insertMaintenance_bp = Blueprint('insertMaintenance', __name__)

@insertMaintenance_bp.route('/api/insertMaintenance', methods=['POST'])
#@role_required(['Admin', 'User'])
def insertWork():
    data = request.get_json()
    resourceId= data.get('resourceId')
    userId= data.get('userId')
    fromDate= data.get('fromDate')
    duration= data.get('duration')
    description= data.get('description')
    maintenancetypeid= data.get('maintenancetypeid')
    
    if not resourceId or not userId or not fromDate or not duration or not description or not maintenancetypeid:
        return jsonify({'error': 'missing input data'}), 400
    new_entry = insertNewMaintenance_service(resourceId, userId, fromDate, duration, description, maintenancetypeid)
    return jsonify({'message': 'entry added', 'maintId': new_entry, 'resourceId': resourceId}), 201

@insertWork_bp.route('/api/insertWork', methods=['POST'])
#@role_required(['Admin', 'User'])
def insertWork():
    data = request.get_json()
    resourceId= data.get('resourceId')
    userId= data.get('userId')
    fromDate= data.get('fromDate')
    duration= data.get('duration')
    
    if not resourceId or not userId or not fromDate or not duration:
        return jsonify({'error': 'missing input data'}), 400
    new_entry = insertNewScheduledWork_service(resourceId, userId, fromDate, duration)
    return jsonify({'message': 'entry added', 'workId': new_entry, 'resourceId': resourceId}), 201