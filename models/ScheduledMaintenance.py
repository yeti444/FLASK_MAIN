class ScheduledMaintenance:
    def __init__(self, maintId, userId, fromDate, duration, createDate, description, maintenancetypeid):
        self._maintId = maintId
        self._userId = userId
        self._fromDate = fromDate
        self._duration = duration
        self._createDate = createDate
        self._description = description
        self._maintenancetypeid = maintenancetypeid

        