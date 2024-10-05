from repository.ScheduledWorkRepository import create_ScheduledWork
from repository.ScheduledResourcesRepository import create_ScheduledResources

def insertNewScheduledWork_service(resourceId, userId, fromDate, duration):
    workId = create_ScheduledWork(userId, fromDate, duration)
    create_ScheduledResources(workId, resourceId)
    return workId