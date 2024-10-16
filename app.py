from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS


from controller.ResourceTypes_Routes import ResourceTypes_bp
from controller.UserRoles_Routes import UserRoles_bp
from controller.UserData_Routes import UserData_bp
from controller.Resources_Routes import Resources_bp
from controller.ScheduledWork_Routes import ScheduledWork_bp
from controller.ScheduledMaintenance_Routes import ScheduledMaintenance_bp
from controller.MaintanedResources_Routes import MaintanedResources_bp
from controller.ScheduledResources_Routes import ScheduledResources_bp

from controller.Insert_Routes import insertWork_bp, insertMaintenance_bp
from controller.CheckAvailability_Routes import checkAvailability_bp


app = Flask(__name__)
jwt = JWTManager(app)
CORS(app)



app.register_blueprint(ResourceTypes_bp)
app.register_blueprint(UserRoles_bp)
app.register_blueprint(UserData_bp)
app.register_blueprint(Resources_bp)
app.register_blueprint(ScheduledWork_bp)
app.register_blueprint(ScheduledMaintenance_bp)
app.register_blueprint(MaintanedResources_bp)
app.register_blueprint(ScheduledResources_bp)

app.register_blueprint(insertWork_bp)
app.register_blueprint(insertMaintenance_bp)
app.register_blueprint(checkAvailability_bp)

if __name__ == '__main__':
    app.run(port=6000, debug=True)