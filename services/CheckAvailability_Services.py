from repository.MaintanedResources_Repository import get_all_MaintanedResources_time
from repository.ScheduledResources_Repository import get_all_ScheduledResources_time
from repository.Resources_Repository import get_all_Resources
from utils.utils import is_overlap, string_to_datetime, string_to_timedelta

def check_time(resourceId, fromDate, duration):
    
                
    S_Resources = get_all_ScheduledResources_time()
    M_Resources = get_all_MaintanedResources_time()
    
    datetime_fromDate = string_to_datetime(fromDate)
    timedelta_duration = string_to_timedelta(duration)
    

    
    for single in S_Resources:
        if single.resourceId == int(resourceId):
            if is_overlap(datetime_fromDate, timedelta_duration, single.fromdate, single.duration):
                return {
                "occupied": True,
                "where": "maintain"
                }
                
    
    for single in M_Resources:
        if single.resourceId == int(resourceId):
            if is_overlap(datetime_fromDate, timedelta_duration, single.fromdate, single.duration):
                return {
                "occupied": True,
                "where": "work"
                }
    return {
    "occupied": False,
    "where": "nowhere"
    }

def check_resource(fromDate, duration):
    A_Resources = get_all_Resources()
    F_Resources = []
    
    for res in A_Resources:
        check_result = check_time(res.resourceId, fromDate, duration)
        if not check_result["occupied"]:
            F_Resources.append(res)

    return F_Resources



            
    

