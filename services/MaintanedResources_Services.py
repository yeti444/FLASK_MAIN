from repository.MaintanedResources_Repository import get_all_MaintanedResources, get_one_MaintanedResources, create_MaintanedResources, update_MaintanedResources, delete_MaintanedResources

def get_all_MaintanedResources_service():
    return get_all_MaintanedResources()

def get_one_MaintanedResources_service(maintId, resourceId):
    return get_one_MaintanedResources(maintId, resourceId)

def create_MaintanedResources_service(maintId, resourceId):
    return create_MaintanedResources(maintId, resourceId)

def update_MaintanedResources_service(maintId, resourceId):
    return update_MaintanedResources(maintId, resourceId)

def delete_MaintanedResources_service(maintId, resourceId):
    return delete_MaintanedResources(maintId, resourceId)
