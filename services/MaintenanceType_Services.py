from repository.MaintenanceType_Repository import get_all_MaintenanceType, get_one_MaintenanceType, create_MaintenanceType, update_MaintenanceType, delete_MaintenanceType

def get_all_MaintenanceType_service():
    return get_all_MaintenanceType()

def get_one_MaintenanceType_service(maintenanceTypeId):
    return get_one_MaintenanceType(maintenanceTypeId)

def create_MaintenanceType_service(typeName):
    return create_MaintenanceType(typeName)

def update_MaintenanceType_service(maintenanceTypeId, typeName):
    return update_MaintenanceType(maintenanceTypeId, typeName)

def delete_MaintenanceType_service(maintenanceTypeId):
    return delete_MaintenanceType(maintenanceTypeId)