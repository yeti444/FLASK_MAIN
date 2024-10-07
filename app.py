from flask import Flask
import importlib

blueprint_modules = [
    ('controller.ResourceTypes_Routes', ['ResourceTypes_bp']),
    ('controller.UserRoles_Routes', ['UserRoles_bp']),
    ('controller.UserData_Routes', ['UserData_bp']),
    ('controller.Resources_Routes', ['Resources_bp']),
    ('controller.ScheduledWork_Routes', ['ScheduledWork_bp']),
    ('controller.ScheduledMaintenance_Routes', ['ScheduledMaintenance_bp']),
    ('controller.MaintanedResources_Routes', ['MaintanedResources_bp']),
    ('controller.ScheduledResources_Routes', ['ScheduledResources_bp']),
    ('controller.insertWork_Routes', ['insertWork_bp']),
    ('controller.insertMaintenance_Routes', ['insertMaintenance_bp']),
    ('controller.checkAvailability_Routes', ['checkAvailability_bp']),
]

app = Flask(__name__)

for module_name, blueprint_names in blueprint_modules:
    module = importlib.import_module(module_name)
    for blueprint_name in blueprint_names:
        blueprint = getattr(module, blueprint_name)
        app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(port=6000, debug=True)
