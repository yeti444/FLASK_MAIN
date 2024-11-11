from repository.ScheduledResources_Repository import get_all_ScheduledResources, get_one_ScheduledResources, create_ScheduledResources, update_ScheduledResources, delete_ScheduledResources

def get_all_ScheduledResources_service():
    return get_all_ScheduledResources()

def get_one_ScheduledResources_service(workId, resourceId):
    return get_one_ScheduledResources(workId, resourceId)

def create_ScheduledResources_service(workId, resourceId):
    return create_ScheduledResources(workId, resourceId)

def update_ScheduledResources_service(new_workId, new_resourceId, workId, resourceId):
    return update_ScheduledResources(new_workId, new_resourceId, workId, resourceId)

def delete_ScheduledResources_service(workId, resourceId):
    return delete_ScheduledResources(workId, resourceId)
