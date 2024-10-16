class ScheduledResources:
    def __init__(self, workId, resourceId):
        self.__workId = workId
        self.__resourceId = resourceId
    
    @property
    def workId(self):
        return self.__workId
    
    @property
    def resourceId(self):
        return self.__resourceId
    
    def to_dict(self):
        return {
            "workId": self.__workId,
            "resourceId": self.__resourceId
        }
    
class ScheduledResources_time:
    def __init__(self, workId, resourceId, fromdate, duration):
        self.__workId = workId
        self.__resourceId = resourceId
        self.__fromdate = fromdate
        self.__duration = duration     
    
    @property
    def workId(self):
        return self.__workId
    
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
            "workId": self.__workId,
            "resourceId": self.__resourceId,
            "fromdate": self.__fromdate,
            "duration": self.__duration
        }        