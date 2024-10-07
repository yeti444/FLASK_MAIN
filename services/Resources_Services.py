from repository.Resources_Repository import get_all_Resources, get_one_Resources, create_Resources, update_Resources, delete_Resources

def get_all_Resources_Service():
    return get_all_Resources()

def get_one_Resources_service(resourceId):
    return get_one_Resources(resourceId)

def create_Resources_service(name, typeId, info):
    return create_Resources(name, typeId, info)

def update_Resources_service(resourceId, name, typeId, info):
    return update_Resources(resourceId, name, typeId, info)

def delete_Resources_service(resourceId):
    return delete_Resources(resourceId)
