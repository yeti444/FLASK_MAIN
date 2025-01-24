from flask import Blueprint, jsonify, request
from services.UserData_Services import get_all_UserData_service, get_one_UserData_service, create_UserData_service, update_UserData_service, delete_UserData_service, login_UserData_service, update_Password_service
from services.UserRoles_Services import get_one_UserRoles_service
from utils.utils import role_required
from flasgger import swag_from
from flask_jwt_extended import get_jwt_identity, create_access_token


UserData_bp = Blueprint('UserData', __name__)

def validate_all(data):
    requiredFields = ['email', 'firstName', 'lastName', 'password', 'roleId']
    for field in requiredFields:
        if field not in data:
            return False, f"Missing input data: {field}"
    return True, ""

def validate_some(data):
    requiredFields = ['email', 'firstName', 'lastName', 'roleId']
    for field in requiredFields:
        if field not in data:
            return False, f"Missing input data: {field}"
    return True, ""

def validate_password(data):
    if 'password' not in data:
        return False, "Missing input data: password"
    return True, ""



@UserData_bp.route('/api/UserData', methods=['GET'])
@role_required(['User', 'Admin'])
@swag_from({
    'tags': ['userData'],
    'description': 'Get a list of all user data.',
    'parameters': [
        {
            'name': 'Authorization',
            'in': 'header',
            'type': 'string',
            'required': True,
            'description': 'Bearer token for authorization'
        }
    ],
    'responses': {
        '200': {
            'description': 'A list of user data.',
            'examples': {
                'application/json': {
                    'UserData': {
                        '1': {
                            'email': 'user@example.com',
                            'firstName': 'John',
                            'lastName': 'Doe',
                            'roleId': 2
                        },
                        '2': {
                            'email': 'admin@example.com',
                            'firstName': 'Admin',
                            'lastName': 'User',
                            'roleId': 1
                        }
                    }
                }
            }
        }
    }
})
def get_UserData():
    entries = get_all_UserData_service()
    user_data_dict = {entry.userId: entry.to_dict() for entry in entries}
    return jsonify({'UserData': user_data_dict})

@UserData_bp.route('/api/UserData/<int:userId>', methods=['GET'])
@role_required(['User', 'Admin'])
@swag_from({
    'tags': ['userData'],
    'description': 'Get user data by userId.',
    'parameters': [
        {
            'name': 'Authorization',
            'in': 'header',
            'type': 'string',
            'required': True,
            'description': 'Bearer token for authorization'
        },
        {
            'name': 'userId',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'The ID of the user whose data is being requested.'
        }
    ],
    'responses': {
        '200': {
            'description': 'User data retrieved successfully.',
            'examples': {
                'application/json': {
                    'email': 'user@example.com',
                    'firstName': 'John',
                    'lastName': 'Doe',
                    'roleId': 2
                }
            }
        },
        '404': {
            'description': 'User not found.',
            'examples': {
                'application/json': {
                    'message': 'User data not found'
                }
            }
        }
    }
})
def get_one_UserData(userId):
    entry = get_one_UserData_service(userId)
    if entry:
        return jsonify(entry.to_dict())
    else:
        return jsonify({'message': 'User data not found'}), 404

@UserData_bp.route('/api/UserData', methods=['POST'])
@swag_from({
    'tags': ['userData'],
    'description': 'Create a new user.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'description': 'User data to be added.',
            'schema': {
                'type': 'object',
                'properties': {
                    'email': {
                        'type': 'string',
                        'description': 'Email address of the user'
                    },
                    'firstName': {
                        'type': 'string',
                        'description': 'First name of the user'
                    },
                    'lastName': {
                        'type': 'string',
                        'description': 'Last name of the user'
                    },
                    'password': {
                        'type': 'string',
                        'description': 'Password for the user account'
                    },
                    'roleId': {
                        'type': 'integer',
                        'description': 'Role ID associated with the user'
                    }
                },
                'example': {
                    'email': 'newuser@example.com',
                    'firstName': 'John',
                    'lastName': 'Doe',
                    'password': 'SecurePassword123$',
                    'roleId': 2
                }
            }
        }
    ],
    'responses': {
        '201': {
            'description': 'User created successfully.',
            'examples': {
                'application/json': {
                    'message': 'Entry added',
                    'userId': 101
                }
            }
        },
        '400': {
            'description': 'Bad Request due to missing or invalid input data.',
            'examples': {
                'application/json': {
                    'error': 'Missing input data: email'
                }
            }
        },
        '500': {
            'description': 'Internal Server Error.',
            'examples': {
                'application/json': {
                    'error': 'Could not create userData',
                    'details': 'Some internal server error message'
                }
            }
        }
    }
})
def create_UserData():
    data = request.get_json()
    is_valid, error_msg = validate_all(data)
    if not is_valid:
        return jsonify({'error': error_msg}), 400

    try:
        new_entry = create_UserData_service(data['email'], data['firstName'], data['lastName'], data['password'], data['roleId'])
        return jsonify({'message': 'Entry added', 'userId': new_entry}), 201
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': 'Could not create userData', 'details': str(e)}), 500



@UserData_bp.route('/api/UserData/<int:userId>', methods=['PUT'])
@role_required(['Admin', 'User'])
@swag_from({
    'tags': ['userData'],
    'description': 'Update user data by userId. Only Admins and Users can perform this action.',
    'parameters': [
        {
            'name': 'Authorization',
            'in': 'header',
            'type': 'string',
            'required': True,
            'description': 'Bearer token for authorization'
        },
        {
            'name': 'userId',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'The ID of the user whose data is being updated.'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'description': 'User data to update.',
            'schema': {
                'type': 'object',
                'properties': {
                    'email': {
                        'type': 'string',
                        'description': 'Updated email address of the user'
                    },
                    'firstName': {
                        'type': 'string',
                        'description': 'Updated first name of the user'
                    },
                    'lastName': {
                        'type': 'string',
                        'description': 'Updated last name of the user'
                    },
                    'roleId': {
                        'type': 'integer',
                        'description': 'Updated role ID associated with the user'
                    }
                },
                'example': {
                    'email': 'updateduser@example.com',
                    'firstName': 'Jane',
                    'lastName': 'Doe',
                    'roleId': 3
                }
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'User updated successfully.',
            'examples': {
                'application/json': {
                    'message': 'Update successful',
                    'userId': 101,
                    'email': 'updateduser@example.com',
                    'token': 'newGeneratedAccessToken'
                }
            }
        },
        '400': {
            'description': 'Bad Request due to missing or invalid input data.',
            'examples': {
                'application/json': {
                    'error': 'Missing input data: email'
                }
            }
        },
        '403': {
            'description': 'Unauthorized action.',
            'examples': {
                'application/json': {
                    'error': 'Unauthorized'
                }
            }
        },
        '404': {
            'description': 'User data not found.',
            'examples': {
                'application/json': {
                    'error': 'User data not found'
                }
            }
        },
        '500': {
            'description': 'Internal Server Error.',
            'examples': {
                'application/json': {
                    'error': 'Could not update userData',
                    'details': 'Some internal server error message'
                }
            }
        }
    }
})
def update_UserData(userId):
    data = request.get_json()
    current_user = get_jwt_identity() 
    curr_userId = current_user['userId']
    curr_role = get_one_UserRoles_service(current_user['roleId']).roleName

    is_valid, error_msg = validate_some(data)
    if not is_valid:
        return jsonify({'error': error_msg}), 400

    existing_user = get_one_UserData_service(userId)
    if not existing_user:
        return jsonify({'error': 'User data not found'}), 404

    try:
        update_UserData_service(data['email'], data['firstName'], data['lastName'], data['roleId'], userId, curr_userId, curr_role)
        new_token = create_access_token(identity=current_user)
        return jsonify({'message': 'Update successful', 'userId': userId, 'email': data['email'], 'token': new_token}), 200
    except ValueError as ve:
        if str(ve) == 'Unauthorized':
            return jsonify({'error': str(ve)}), 403
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': 'Could not update userData', 'details': str(e)}), 500


@UserData_bp.route('/api/changePassword/<int:userId>', methods=['PUT'])
@role_required(['Admin', 'User'])
@swag_from({
    'tags': ['userData'],
    'description': 'Update the password of a user by userId. Only Admins and Users can perform this action.',
    'parameters': [
        {
            'name': 'Authorization',
            'in': 'header',
            'type': 'string',
            'required': True,
            'description': 'Bearer token for authorization'
        },
        {
            'name': 'userId',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'The ID of the user whose password is being updated.'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'description': 'Password data to update.',
            'schema': {
                'type': 'object',
                'properties': {
                    'password': {
                        'type': 'string',
                        'description': 'The new password for the user account'
                    }
                },
                'example': {
                    'password': 'NewSecurePassword123'
                }
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'Password updated successfully.',
            'examples': {
                'application/json': {
                    'message': 'Update successful',
                    'userId': 101,
                    'token': 'newGeneratedAccessToken'
                }
            }
        },
        '400': {
            'description': 'Bad Request due to missing or invalid input data.',
            'examples': {
                'application/json': {
                    'error': 'Missing input data: password'
                }
            }
        },
        '404': {
            'description': 'User data not found.',
            'examples': {
                'application/json': {
                    'error': 'User data not found'
                }
            }
        },
        '500': {
            'description': 'Internal Server Error.',
            'examples': {
                'application/json': {
                    'error': 'Could not update userData',
                    'details': 'Some internal server error message'
                }
            }
        }
    }
})
def update_Password(userId):
    data = request.get_json()
    current_user = get_jwt_identity() 

    is_valid, error_msg = validate_password(data)
    if not is_valid:
        return jsonify({'error': error_msg}), 400

    existing_user = get_one_UserData_service(userId)
    if not existing_user:
        return jsonify({'error': 'User data not found'}), 404

    try:
        update_Password_service(data['password'], userId)
        new_token = create_access_token(identity=current_user)
        return jsonify({'message': 'Update successful', 'userId': userId, 'token': new_token}), 200
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': 'Could not update userData', 'details': str(e)}), 500

@UserData_bp.route('/api/UserData/<int:userId>', methods=['DELETE'])
@role_required(['User', 'Admin'])
@swag_from({
    'tags': ['userData'],
    'description': 'Delete user data by userId. Only Admins and Users can perform this action.',
    'parameters': [
        {
            'name': 'Authorization',
            'in': 'header',
            'type': 'string',
            'required': True,
            'description': 'Bearer token for authorization'
        },
        {
            'name': 'userId',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'The ID of the user whose data is being deleted.'
        }
    ],
    'responses': {
        '200': {
            'description': 'User data deleted successfully.',
            'examples': {
                'application/json': {
                    'message': 'userData deleted successfully',
                    'userId': 101
                }
            }
        },
        '404': {
            'description': 'User data not found.',
            'examples': {
                'application/json': {
                    'error': 'User data not found'
                }
            }
        },
        '500': {
            'description': 'Internal Server Error.',
            'examples': {
                'application/json': {
                    'error': 'Could not delete userData',
                    'details': 'Some internal server error message'
                }
            }
        }
    }
})
def delete_UserData(userId):
    existing_data = get_one_UserData_service(userId)
    if existing_data:
        try:
            delete_UserData_service(userId)
            return jsonify({'message': 'userData deleted successfully', 'userId': userId}), 200
        except Exception as e:
            return jsonify({'error': 'Could not delete userData', 'details': str(e)}), 500
    return jsonify({'error': 'User data not found'}), 404


@UserData_bp.route('/api/login', methods=['POST'])
@swag_from({
    'tags': ['Beléptető'],
    'description': 'Log in a user and return an authentication token.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'description': 'User login credentials.',
            'schema': {
                'type': 'object',
                'properties': {
                    'email': {
                        'type': 'string',
                        'description': 'Email address of the user'
                    },
                    'password': {
                        'type': 'string',
                        'description': 'Password of the user'
                    }
                },
                'example': {
                    'email': 'user@example.com',
                    'password': 'SecurePassword123'
                }
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'Login successful.',
            'examples': {
                'application/json': {
                    'message': 'Login successful',
                    'token': 'eyJhbGciOiJIUzI1NiIsInR...',
                    'userId': 101,
                    'email': 'user@example.com',
                    'roleName': 'User'
                }
            }
        },
        '400': {
            'description': 'Bad Request due to missing email or password.',
            'examples': {
                'application/json': {
                    'error': 'Missing email or password'
                }
            }
        },
        '401': {
            'description': 'Unauthorized access due to invalid credentials.',
            'examples': {
                'application/json': {
                    'error': 'Invalid email or password'
                }
            }
        },
        '500': {
            'description': 'Internal Server Error.',
            'examples': {
                'application/json': {
                    'error': 'Unknown',
                    'details': 'Some internal server error message'
                }
            }
        }
    }
})
def login_UserData():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({'error': 'Missing email or password'}), 400
    
    try:
        login_data = login_UserData_service(email, password)
        return jsonify({
            'message': 'Login successful',
            'token': login_data['token'],
            'userId': login_data['userId'],
            'email': login_data['email'],
            'roleName': login_data['roleName']
        }), 200
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 401
    except Exception as e:
        return jsonify({'error': 'Unknown', 'details': str(e)}), 500

