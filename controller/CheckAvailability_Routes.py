from flask import Blueprint, jsonify, request
from services.CheckAvailability_Services import check_time
from services.Resources_Services import get_one_Resources_service

from utils.utils import role_required
from flasgger import swag_from

checkAvailability_bp = Blueprint('checkAvailability', __name__)

@checkAvailability_bp.route('/api/checkAvailability/<int:resourceId>', methods=['GET'])
#@role_required(['Admin', 'User'])
@swag_from({
    'tags': ['checkAvailability'],
    'description': 'Check the availability of a resource based on resource ID, date, and interval.',
    'parameters': [
        {
            'name': 'resourceId',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'The ID of the resource to check availability for.',
            'schema': {
                'type': 'integer',
                'example': '1'
            }
        },
        {
            'name': 'date',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': 'The date to check availability (format: YYYY-MM-DDTHH:MM:SS). Default is the current date and time.',
            'schema': {
                'type': 'string',
                'example': '2024-10-08T11:00:00'
            }
        },
        {
            'name': 'interval',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': 'The time interval to check availability for (format: HH:MM:SS). Default is 01:00:00.',
            'schema': {
                'type': 'string',
                'example': '01:00:00'
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'The availability of the resource based on the given parameters.',
            'examples': {
                'application/json': {
                    'occupied': True,
                    'where': 'work'
                }
            }
        },
        '404': {
            'description': 'Resource not found for the given resource ID.',
            'examples': {
                'application/json': {
                    'message': 'Resource with the given ID not found.'
                }
            }
        },
        '500': {
            'description': 'Internal Server Error, unexpected failure.',
            'examples': {
                'application/json': {
                    'message': 'Internal Server Error: Something went wrong.'
                }
            }
        }
    }
})
def get_MaintanedResources(resourceId):
    date = request.args.get('date')
    interval = request.args.get('interval', "01:00:00")
    
    try:
        result = check_time(resourceId, date, interval)
        existing_Resources = get_one_Resources_service(resourceId)
        
        if existing_Resources:
            return jsonify(result), 200
        else:
            return jsonify({'message': f'Resource with ID {resourceId} not found.'}), 404
    except Exception as e:
        return jsonify({'message': f'Internal Server Error: {str(e)}'}), 500
