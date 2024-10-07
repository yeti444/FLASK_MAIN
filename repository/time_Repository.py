from datetime import datetime, timedelta
import re
import pytz

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