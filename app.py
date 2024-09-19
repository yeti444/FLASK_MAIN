from flask import Flask
from routes.ResourceTypesRoutes import ResourceTypes_bp
from routes.UserRolesRoutes import UserRoles_bp

app = Flask(__name__)
app.register_blueprint(ResourceTypes_bp)
app.register_blueprint(UserRoles_bp)

if __name__ == '__main__':
    app.run(port=6000, debug=True)
    