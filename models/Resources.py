class Resources:
    def __init__(self, resourceId, name, typeId, info, createDate):
        self.__resourceId = resourceId
        self.__name = name
        self.__typeId = typeId
        self.__info = info
        self.__createDate = createDate

    @property
    def resourceId(self):
        return self.__resourceId
    
    @property
    def name(self):
        return self.__name

    @property
    def typeId(self):
        return self.__typeId

    @property
    def info(self):
        return self.__info
    
    @property
    def createDate(self):
        return self.__createDate
    
    def to_dict(self):
        return {
            "resourceId": self.__resourceId,
            "name": self.__name,
            "typeId": self.__typeId,
            "info": self.__info,
            "createDate": self.__createDate
        }