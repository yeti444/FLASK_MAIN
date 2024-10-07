from repository.MaintanedResources_Repository import get_all_MaintanedResources_time
from repository.ScheduledResources_Repository import get_all_ScheduledResources_time
from repository.checkAvailability_Repository import is_overlap
from repository.time_Repository import string_to_datetime, string_to_timedelta


def check_time(resourceId, fromDate, duration):
    
                
    S_Resources = get_all_ScheduledResources_time()
    M_Resources = get_all_MaintanedResources_time()

    print(duration)
    
    datetime_fromDate = string_to_datetime(fromDate)
    timedelta_duration = string_to_timedelta(duration)
    

    
    for single in S_Resources:
        if single.get_resourceId() is int(resourceId):
            if is_overlap(datetime_fromDate, timedelta_duration, single.fromdate(), single.duration()):
                return True
                
    
    for single in M_Resources:
        if single.get_resourceId() is int(resourceId):
            if is_overlap(datetime_fromDate, timedelta_duration, single.fromdate(), single.duration()):
                return True
    return False

