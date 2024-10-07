from repository.UserRoles_Repository import get_all_UserRoles, get_one_UserRoles, update_UserRoles, create_UserRoles, delete_UserRoles

def get_all_UserRoles_service():
    return get_all_UserRoles()

def get_one_UserRoles_service(roleId):
    return get_one_UserRoles(roleId)

def create_UserRoles_service(roleName):
    return create_UserRoles(roleName)

def update_UserRoles_service(roleId, roleName):
    return update_UserRoles(roleId, roleName)

def delete_UserRoles_service(roleId):
    return delete_UserRoles(roleId)