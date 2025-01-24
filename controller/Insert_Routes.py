from flask import Blueprint, jsonify, request
from services.Insert_Services import insertNewScheduledWork_service, insertNewMaintenance_service
from utils.utils import role_required
from flasgger import swag_from

insertWork_bp = Blueprint('inserWork', __name__)
insertMaintenance_bp = Blueprint('insertMaintenance', __name__)

@insertMaintenance_bp.route('/api/insertMaintenance', methods=['POST'])
#@role_required(['Admin', 'User'])
@swag_from({
    'tags': ['insert'],
    'description': 'Insert a new maintenance entry with required details.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'description': 'Maintenance entry data',
            'schema': {
                'type': 'object',
                'properties': {
                    'resourceId': {
                        'type': 'integer',
                        'example': 1
                    },
                    'userId': {
                        'type': 'integer',
                        'example': 1
                    },
                    'fromDate': {
                        'type': 'string',
                        'example': '2024-10-25T09:00:00Z'
                    },
                    'duration': {
                        'type': 'string',
                        'example': '3'
                    },
                    'description': {
                        'type': 'string',
                        'example': 'Annual maintenance check'
                    },
                    'maintenancetypeid': {
                        'type': 'integer',
                        'example': 1
                    }
                },
                'required': ['resourceId', 'userId', 'fromDate', 'duration', 'description', 'maintenancetypeid']
            }
        }
    ],
    'responses': {
        '201': {
            'description': 'Maintenance entry successfully added.',
            'examples': {
                'application/json': {
                    'message': 'entry added',
                    'maintId': 123,
                    'resourceId': 1
                }
            }
        },
        '400': {
            'description': 'Bad request due to missing or invalid input data.',
            'examples': {
                'application/json': {
                    'error': 'missing input data'
                }
            }
        },
        '500': {
            'description': 'Internal Server Error.',
            'examples': {
                'application/json': {
                    'error': 'Internal Server Error: <error_message>'
                }
            }
        }
    }
})
def insertWork():
    data = request.get_json()

    resourceId = data.get('resourceId')
    userId = data.get('userId')
    fromDate = data.get('fromDate')
    duration = data.get('duration')
    description = data.get('description')
    maintenancetypeid = data.get('maintenancetypeid')

    if not resourceId or not userId or not fromDate or not duration or not description or not maintenancetypeid:
        return jsonify({'error': 'missing input data'}), 400

    try:
        new_entry = insertNewMaintenance_service(resourceId, userId, fromDate, duration, description, maintenancetypeid)
        return jsonify({'message': 'entry added', 'maintId': new_entry, 'resourceId': resourceId}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@insertWork_bp.route('/api/insertWork', methods=['POST'])
#@role_required(['Admin', 'User'])
@swag_from({
    'tags': ['insert'],
    'description': 'Insert a new work entry with required details.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'description': 'Work entry data',
            'schema': {
                'type': 'object',
                'properties': {
                    'resourceId': {
                        'type': 'integer',
                        'example': 1
                    },
                    'userId': {
                        'type': 'integer',
                        'example': 1
                    },
                    'fromDate': {
                        'type': 'string',
                        'example': '2024-10-25T09:00:00Z'
                    },
                    'duration': {
                        'type': 'string',
                        'example': '3'
                    }
                },
                'required': ['resourceId', 'userId', 'fromDate', 'duration']
            }
        }
    ],
    'responses': {
        '201': {
            'description': 'Work entry successfully added.',
            'examples': {
                'application/json': {
                    'message': 'entry added',
                    'workId': 456,
                    'resourceId': 1
                }
            }
        },
        '400': {
            'description': 'Bad request due to missing or invalid input data.',
            'examples': {
                'application/json': {
                    'error': 'missing input data'
                }
            }
        },
        '500': {
            'description': 'Internal Server Error.',
            'examples': {
                'application/json': {
                    'error': 'Internal Server Error: <error_message>'
                }
            }
        }
    }
})
def insertWork():
    data = request.get_json()

    resourceId = data.get('resourceId')
    userId = data.get('userId')
    fromDate = data.get('fromDate')
    duration = data.get('duration')

    if not resourceId or not userId or not fromDate or not duration:
        return jsonify({'error': 'missing input data'}), 400

    try:
        new_entry = insertNewScheduledWork_service(resourceId, userId, fromDate, duration)
        return jsonify({'message': 'entry added', 'workId': new_entry, 'resourceId': resourceId}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
