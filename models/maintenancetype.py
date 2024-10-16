class MaintenanceType:
    def __init__(self, maintenanceTypeId, typeName):
        self.__maintenanceTypeId = maintenanceTypeId
        self.__typeName = typeName

    @property
    def maintenanceTypeId(self):
        return self.__maintenanceTypeId
    
    @property
    def typeName(self):
        return self.__typeName
    
    def to_dict(self):
        return {
            "maintenanceTypeId": self.__maintenanceTypeId,
            "typeName": self.__typeName
        }