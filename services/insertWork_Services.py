from repository.ScheduledWork_Repository import create_ScheduledWork
from repository.ScheduledResources_Repository import create_ScheduledResources

def insertNewScheduledWork_service(resourceId, userId, fromDate, duration):
    workId = create_ScheduledWork(userId, fromDate, duration)
    create_ScheduledResources(workId, resourceId)
    return workId