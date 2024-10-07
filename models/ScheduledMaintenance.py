class ScheduledMaintenance:
    def __init__(self, maintId, userId, fromDate, duration, createDate, description, maintenancetypeid):
        self.maintId = maintId
        self.userId = userId
        self.fromDate = fromDate
        self.duration = duration
        self.createDate = createDate
        self.description = description
        self.maintenancetypeid = maintenancetypeid

        