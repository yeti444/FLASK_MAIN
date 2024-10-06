class MaintanedResources:
    def __init__(self, maintId, resourceId):
        self._maintId = maintId
        self._resourceId = resourceId
        
class MaintanedResources_time:
    def __init__(self, maintId, resourceId, fromdate, duration):
        self._maintId = maintId
        self._resourceId = resourceId
        self._fromdate = fromdate
        self._duration = duration     
    def get_resourceId(self):
        return self._resourceId  
    def get_fromdate(self):
        return self._fromdate  
    def get_duration(self):
        return self._duration  
    