from repository.ScheduledMaintenance_Repository import get_all_ScheduledMaintenance, get_one_ScheduledMaintenance, create_ScheduledMaintenance, update_ScheduledMaintenance, delete_ScheduledMaintenance
from utils.utils import calculate_status

def get_all_ScheduledMaintenance_service():
    entries = get_all_ScheduledMaintenance()
    for entry in entries:
        entry.status = calculate_status(entry)
    return entries

def get_one_ScheduledMaintenance_service(workId):
    entry = get_one_ScheduledMaintenance(workId)
    if entry:
        entry.status = calculate_status(entry)
    return entry

def create_ScheduledMaintenance_service(userId, fromDate, duration, description, maintenancetypeid):
    return create_ScheduledMaintenance(userId, fromDate, duration, description, maintenancetypeid)

def update_ScheduledMaintenance_service(maintId, userId, fromDate, duration, description, maintenancetypeid):
    updated_entry = update_ScheduledMaintenance(maintId, userId, fromDate, duration, description, maintenancetypeid)
    if updated_entry:
        updated_entry.status = calculate_status(updated_entry)
    return updated_entry

def delete_ScheduledMaintenance_service(maintId):
    return delete_ScheduledMaintenance(maintId)
