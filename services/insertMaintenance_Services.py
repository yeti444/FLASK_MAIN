from repository.ScheduledMaintenance_Repository import create_ScheduledMaintenance
from repository.MaintanedResources_Repository import create_MaintanedResources

def insertNewMaintenance_service(resourceId, userId, fromDate, duration, description, maintenancetypeid):
    maintId = create_ScheduledMaintenance(userId, fromDate, duration, description, maintenancetypeid)
    create_MaintanedResources(maintId, resourceId)
    return maintId