from datetime import datetime, timedelta
import re
import pytz
import bcrypt

from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from functools import wraps
from services.UserRoles_Services import get_one_UserRoles_service



def validate_user_data(email, password):
    if not is_valid_email(email):
        raise ValueError('Invalid email format')
    if not is_password_strong(password):
        raise ValueError('Invalid password')

def role_required(allowed_roles):
    def wrapper(fn):
        @wraps(fn)
        @jwt_required()
        def decorated_view(*args, **kwargs):
            current_user = get_jwt_identity()
            role_id = current_user['roleId']
            role_name = get_one_UserRoles_service(role_id).roleName

            if role_name not in allowed_roles and role_name != 'Admin':
                return jsonify({'error': 'Unauthorized'}), 403
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

def calculate_status(entry):
    timezone = entry.fromDate.tzinfo
    current_time = datetime.now(timezone)
    start_time = entry.fromDate
    end_time = start_time + entry.duration
    if current_time < start_time:
        return "Pending"
    elif start_time <= current_time <= end_time:
        return "Ongoing"
    else:
        return "Done"
    
def is_overlap(start1, duration1, start2, duration2):
    end1 = start1 + duration1
    end2 = start2 + duration2
    return start1 <= end2 and start2 <= end1

def string_to_timedelta(duration_str):
    total_delta = timedelta()
    regex_patterns = {
        'days': r'(-?\d+)\s*days?',
        'hours': r'(-?\d+)\s*hours?',
        'minutes': r'(-?\d+)\s*minutes?',
        'seconds': r'(-?\d+)\s*seconds?'
    }
    for unit, pattern in regex_patterns.items():
        match = re.search(pattern, duration_str)
        if match:
            value = int(match.group(1))
            total_delta += timedelta(**{unit: value})

    return total_delta

def string_to_datetime(date_str, timezone_str='Europe/Budapest'):
    naive_dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
    tz = pytz.timezone(timezone_str)
    aware_dt = tz.localize(naive_dt)
    return aware_dt

def hashPassword(password):
    byte_password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(byte_password, salt)
    return hashed_password

def checkPassword(password, hashed_password):
    byte_password = password.encode('utf-8')
    byte_hashed_password = bytes.fromhex(hashed_password[2:])
    return bcrypt.checkpw(byte_password, byte_hashed_password)


def is_password_strong(password):
    return len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password) and any(not char.isalnum() for char in password)

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None