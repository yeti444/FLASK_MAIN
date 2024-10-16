class MaintanedResources:
    def __init__(self, maintId, resourceId):
        self.__maintId = maintId
        self.__resourceId = resourceId
    
    @property
    def maintId(self):
        return self.__maintId
    
    @property
    def resourceId(self):
        return self.__resourceId
    
    def to_dict(self):
        return {
            "maintId": self.__maintId,
            "resourceId": self.__resourceId
        }
    
class MaintanedResources_time:
    def __init__(self, maintId, resourceId, fromdate, duration):
        self.__maintId = maintId
        self.__resourceId = resourceId
        self.__fromdate = fromdate
        self.__duration = duration     
    
    @property
    def maintId(self):
        return self.__maintId
    
    @property
    def resourceId(self):
        return self.__resourceId

    @property
    def fromdate(self):
        return self.__fromdate

    @property
    def duration(self):
        return self.__duration
    
    def to_dict(self):
        return {
            "maintId": self.__maintId,
            "resourceId": self.__resourceId,
            "fromdate": self.__fromdate,
            "duration": self.__duration
        }