from flask import Flask
from controller.ResourceTypesRoutes import ResourceTypes_bp
from controller.UserRolesRoutes import UserRoles_bp
from controller.UserDataRoutes import UserData_bp
from controller.ResourcesRoutes import Resources_bp
from controller.ScheduledWorkRoutes import ScheduledWork_bp
from controller.ScheduledMaintenanceRoutes import ScheduledMaintenance_bp
from controller.MaintanedResourcesRoutes import MaintanedResources_bp
from controller.ScheduledResourcesRoutes import ScheduledResources_bp

app = Flask(__name__)
app.register_blueprint(ResourceTypes_bp)
app.register_blueprint(UserRoles_bp)
app.register_blueprint(UserData_bp)
app.register_blueprint(Resources_bp)
app.register_blueprint(ScheduledWork_bp)
app.register_blueprint(ScheduledMaintenance_bp)
app.register_blueprint(MaintanedResources_bp)
app.register_blueprint(ScheduledResources_bp)

if __name__ == '__main__':
    app.run(port=6000, debug=True)
    