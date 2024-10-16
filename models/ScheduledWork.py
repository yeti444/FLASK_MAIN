class ScheduledWork:
    def __init__(self, workId, userId, fromDate, duration, createDate):
        self.__workId = workId
        self.__userId = userId
        self.__fromDate = fromDate
        self.__duration = duration
        self.__createDate = createDate
        self.__status = None
    
    @property
    def workId(self):
        return self.__workId
    
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
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    def to_dict(self):
        return {
            "workId": self.__workId,
            "userId": self.__userId,
            "fromDate": self.__fromDate,
            "duration": str(self.__duration),
            "createDate": self.__createDate,
            "status": self.__status,
        }