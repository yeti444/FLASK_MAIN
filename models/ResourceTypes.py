class ResourceTypes:
    def __init__(self, typeId, typeName):
        self.__typeId = typeId
        self.__typeName = typeName
    
    @property
    def typeId(self):
        return self.__typeId

    @property
    def typeName(self):
        return self.__typeName
    
    def to_dict(self):
        return {
            "typeId": self.__typeId,
            "typeName": self.__typeName
        }

        