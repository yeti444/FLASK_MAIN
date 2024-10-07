from repository.ScheduledMaintenance_Repository import get_all_ScheduledMaintenance, get_one_ScheduledMaintenance, create_ScheduledMaintenance, update_ScheduledMaintenance, delete_ScheduledMaintenance

def get_all_ScheduledMaintenance_service():
    return get_all_ScheduledMaintenance()

def get_one_ScheduledMaintenance_service(workId):
    return get_one_ScheduledMaintenance(workId)

def create_ScheduledMaintenance_service(userId, fromDate, duration, description, maintenancetypeid):
    return create_ScheduledMaintenance(userId, fromDate, duration, description, maintenancetypeid)

def update_ScheduledMaintenance_service(maintId, userId, fromDate, duration, description, maintenancetypeid):
    return update_ScheduledMaintenance(maintId, userId, fromDate, duration, description, maintenancetypeid)

def delete_ScheduledMaintenance_service(maintId):
    return delete_ScheduledMaintenance(maintId)
