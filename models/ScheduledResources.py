class ScheduledResources:
    def __init__(self, workId, resourceId):
        self._workId = workId
        self._resourceId = resourceId
        
class ScheduledResources_time:
    def __init__(self, workId, resourceId, fromdate, duration):
        self._workId = workId
        self._resourceId = resourceId
        self._fromdate = fromdate
        self._duration = duration
    def get_resourceId(self):
        return self._resourceId  
    def get_fromdate(self):
        return self._fromdate  
    def get_duration(self):
        return self._duration          