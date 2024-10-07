class MaintanedResources:
    def __init__(self, maintId, resourceId):
        self.maintId = maintId
        self.resourceId = resourceId
        
class MaintanedResources_time:
    def __init__(self, maintId, resourceId, fromdate, duration):
        self.maintId = maintId
        self.resourceId = resourceId
        self.fromdate = fromdate
        self.duration = duration     
    