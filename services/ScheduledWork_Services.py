from repository.ScheduledWork_Repository import get_all_ScheduledWork, get_one_ScheduledWork, create_ScheduledWork, update_ScheduledWork, delete_ScheduledWork
from utils.utils import calculate_status

def get_all_ScheduledWork_service():
    entries = get_all_ScheduledWork()
    for entry in entries:
        entry.status = calculate_status(entry)
    return entries

def get_one_ScheduledWork_service(workId):
    entry = get_one_ScheduledWork(workId)
    if entry:
        entry.status = calculate_status(entry)
    return entry

def create_ScheduledWork_service(userId, fromDate, duration):
    return create_ScheduledWork(userId, fromDate, duration)

def update_ScheduledWork_service(workId, userId, fromDate, duration):
    updated_entry = update_ScheduledWork(workId, userId, fromDate, duration)
    if updated_entry:
        updated_entry.status = calculate_status(updated_entry)
    return updated_entry

def delete_ScheduledWork_service(workId):
    return delete_ScheduledWork(workId)


