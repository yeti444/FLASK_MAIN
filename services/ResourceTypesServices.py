from repository.ResourceTypesRepository import get_all_ResourceTypes, get_one_ResourceTypes, create_ResourceTypes, update_ResourceTypes, delete_ResourceTypes

def get_all_ResourceTypes_service():
    return get_all_ResourceTypes()

def get_one_ResourceTypes_service(typeId):
    return get_one_ResourceTypes(typeId)

def create_ResourceTypes_service(typeName):
    return create_ResourceTypes(typeName)

def update_ResourceTypes_service(typeId, typeName):
    return update_ResourceTypes(typeId, typeName)

def delete_ResourceTypes_service(typeId):
    return delete_ResourceTypes(typeId)
