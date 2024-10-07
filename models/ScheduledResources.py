class ScheduledResources:
    def __init__(self, workId, resourceId):
        self.workId = workId
        self.resourceId = resourceId
        
class ScheduledResources_time:
    def __init__(self, workId, resourceId, fromdate, duration):
        self.workId = workId
        self.resourceId = resourceId
        self.fromdate = fromdate
        self.duration = duration  