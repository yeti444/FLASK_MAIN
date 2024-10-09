class UserRoles:
    def __init__(self, roleId, roleName):
        self.__roleId = roleId
        self.__roleName = roleName
    
    @property
    def roleId(self):
        return self.__roleId
    
    @property
    def roleName(self):
        return self.__roleName
    
    def to_dict(self):
        return {
            "roleId": self.__roleId,
            "roleName": self.__roleName,
        }    