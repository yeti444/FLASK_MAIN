from repository.ScheduledWorkRepository import get_all_ScheduledWork, get_one_ScheduledWork, create_ScheduledWork, update_ScheduledWork, delete_ScheduledWork

def get_all_ScheduledWork_service():
    return get_all_ScheduledWork()

def get_one_ScheduledWork_service(workId):
    return get_one_ScheduledWork(workId)

def create_ScheduledWork_service(userId, fromDate, duration):
    return create_ScheduledWork(userId, fromDate, duration)

def update_ScheduledWork_service(workId, userId, fromDate, duration):
    return update_ScheduledWork(workId, userId, fromDate, duration)

def delete_ScheduledWork_service(workId):
    return delete_ScheduledWork(workId)
