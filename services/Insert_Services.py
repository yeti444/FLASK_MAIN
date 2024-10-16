from repository.ScheduledMaintenance_Repository import create_ScheduledMaintenance
from repository.MaintanedResources_Repository import create_MaintanedResources
from repository.ScheduledWork_Repository import create_ScheduledWork
from repository.ScheduledResources_Repository import create_ScheduledResources

def insertNewMaintenance_service(resourceId, userId, fromDate, duration, description, maintenancetypeid):
    maintId = create_ScheduledMaintenance(userId, fromDate, duration, description, maintenancetypeid)
    create_MaintanedResources(maintId, resourceId)
    return maintId

def insertNewScheduledWork_service(resourceId, userId, fromDate, duration):
    workId = create_ScheduledWork(userId, fromDate, duration)
    create_ScheduledResources(workId, resourceId)
    return workId