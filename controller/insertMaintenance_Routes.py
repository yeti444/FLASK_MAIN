from flask import Blueprint, jsonify, request
from services.insertMaintenance_Services import insertNewMaintenance_service

insertMaintenance_bp = Blueprint('insertMaintenance_bp', __name__)

@insertMaintenance_bp.route('/api/insertMaintenance', methods=['POST'])
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
    return jsonify({'message': 'entry added', 'maintId': new_entry, 'resourceId': resourceId})  

