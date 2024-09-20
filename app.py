from flask import Flask
from routes.ResourceTypesRoutes import ResourceTypes_bp
from routes.UserRolesRoutes import UserRoles_bp
from routes.UserDataRoutes import UserData_bp

app = Flask(__name__)
app.register_blueprint(ResourceTypes_bp)
app.register_blueprint(UserRoles_bp)
app.register_blueprint(UserData_bp)

if __name__ == '__main__':
    app.run(port=6000, debug=True)
    