class ScheduledMaintenance:
    def __init__(self, maintId, userId, fromDate, duration, createDate, description, maintenancetypeid):
        self.__maintId = maintId
        self.__userId = userId
        self.__fromDate = fromDate
        self.__duration = duration
        self.__createDate = createDate
        self.__description = description
        self.__maintenancetypeid = maintenancetypeid

    @property
    def maintId(self):
        return self.__maintId
    
    @property
    def userId(self):
        return self.__userId
    
    @property
    def fromDate(self):
        return self.__fromDate
    
    @property
    def duration(self):
        return self.__duration
    
    @property
    def createDate(self):
        return self.__createDate
    
    @property
    def description(self):
        return self.__description
    
    @property
    def maintenancetypeid(self):
        return self.__maintenancetypeid
    
    def to_dict(self):
        return {
            "workId": self.__maintId,
            "userId": self.__userId,
            "fromDate": self.__fromDate,
            "duration": str(self.__duration),
            "createDate": self.__createDate,
            "description": self.__description,
            "maintenancetypeid": self.__maintenancetypeid
        }

        