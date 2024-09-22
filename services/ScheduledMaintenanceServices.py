from repository.ScheduledMaintenanceRepository import get_all_ScheduledMaintenance, get_one_ScheduledMaintenance, create_ScheduledMaintenance, update_ScheduledMaintenance, delete_ScheduledMaintenance

def get_all_ScheduledMaintenance_service():
    return get_all_ScheduledMaintenance()

def get_one_ScheduledMaintenance_service(workId):
    return get_one_ScheduledMaintenance(workId)

def create_ScheduledMaintenance_service(userId, fromDate, duration):
    return create_ScheduledMaintenance(userId, fromDate, duration)

def update_ScheduledMaintenance_service(maintId, userId, fromDate, duration):
    return update_ScheduledMaintenance(maintId, userId, fromDate, duration)

def delete_ScheduledMaintenance_service(maintId):
    return delete_ScheduledMaintenance(maintId)
