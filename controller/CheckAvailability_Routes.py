from flask import Blueprint, jsonify, request
from services.CheckAvailability_Services import check_time

from utils.utils import role_required

checkAvailability_bp = Blueprint('checkAvailability', __name__)

@checkAvailability_bp.route('/api/checkAvailability/<int:resourceId>', methods=['GET'])
@role_required(['Admin', 'User'])
def get_MaintanedResources(resourceId):
    date = request.args.get('date')
    interval = request.args.get('interval') 
    return jsonify({'message': check_time(resourceId, date, interval)}), 200