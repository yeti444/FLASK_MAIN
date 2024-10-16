from repository.MaintanedResources_Repository import get_all_MaintanedResources_time
from repository.ScheduledResources_Repository import get_all_ScheduledResources_time
from utils.utils import is_overlap, string_to_datetime, string_to_timedelta

def check_time(resourceId, fromDate, duration):
    
                
    S_Resources = get_all_ScheduledResources_time()
    M_Resources = get_all_MaintanedResources_time()

    print(duration)
    
    datetime_fromDate = string_to_datetime(fromDate)
    timedelta_duration = string_to_timedelta(duration)
    

    
    for single in S_Resources:
        if single.resourceId is int(resourceId):
            if is_overlap(datetime_fromDate, timedelta_duration, single.fromdate, single.duration):
                return True
                
    
    for single in M_Resources:
        if single.resourceId is int(resourceId):
            if is_overlap(datetime_fromDate, timedelta_duration, single.fromdate, single.duration):
                return True
    return False


