from repository.ScheduledMaintenanceRepository import create_ScheduledMaintenance
from repository.MaintanedResourcesRepository import create_MaintanedResources

def insertNewMaintenance_service(resourceId, userId, fromDate, duration, description, maintenancetypeid):
    maintId = create_ScheduledMaintenance(userId, fromDate, duration, description, maintenancetypeid)
    create_MaintanedResources(maintId, resourceId)
    return maintId