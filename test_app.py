import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
        
@pytest.fixture
def jwt_token(client):
    credentials = {
        "email": "kristof20011020@gmail.com",
        "password": "lenin17@"
    }
    response = client.post('/api/login', json=credentials)
    assert response.status_code == 200
    
    token = response.get_json().get('token') 
    return token

        

def test_userData(client, jwt_token):

    response = client.get('/api/UserData', headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 200
    
    response = client.post('/api/UserData', json={
        "email": "testemail@test.com",
        "firstName": "test",
        "lastName": "test",
        "password": "Password@12",
        "roleId": 1
    }, headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 201 
    json_data = response.get_json()
    
    assert "message" in json_data
    assert "userId" in json_data
    assert isinstance(json_data["userId"], int)
    assert json_data["userId"] > 0
    assert json_data["message"] == "Entry added"
    
    userId = json_data["userId"]
    response = client.put(f'/api/UserData/{userId}', json={
        "email": "edit@edit.com",
        "firstName": "edit",
        "lastName": "edit",
        "password": "Password@13",
        "roleId": 1
    }, headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "userId" in json_data
    assert "message" in json_data
    assert isinstance(json_data["userId"], int)
    assert json_data["userId"] > 0
    assert json_data["message"] == "Update successful"
    
    userId = json_data["userId"]
    response = client.delete(f'/api/UserData/{userId}', headers={"Authorization": f"Bearer {jwt_token}"})
    
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "userId" in json_data
    assert "message" in json_data
    assert isinstance(json_data["userId"], int)
    assert json_data["userId"] > 0
    assert json_data["message"] == "userData deleted successfully"

def test_userRoles(client, jwt_token):
    response = client.get('/api/UserRoles', headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 200
    
    response = client.post('/api/UserRoles', json={
        "roleName": "testRole",
    }, headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 201 
    json_data = response.get_json()
    
    assert "message" in json_data
    assert "roleId" in json_data
    assert isinstance(json_data["roleId"], int)
    assert json_data["roleId"] > 0
    assert json_data["message"] == "entry added"
    
    roleId = json_data["roleId"]
    response = client.put(f'/api/UserRoles/{roleId}', json={
        "roleName": "deadbeat",
    }, headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "roleId" in json_data
    assert "message" in json_data
    assert isinstance(json_data["roleId"], int)
    assert json_data["roleId"] > 0
    assert json_data["message"] == "update successful"
    
    roleId = json_data["roleId"]
    response = client.delete(f'/api/UserRoles/{roleId}', headers={"Authorization": f"Bearer {jwt_token}"})
    
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "roleId" in json_data
    assert "message" in json_data
    assert isinstance(json_data["roleId"], int)
    assert json_data["roleId"] > 0
    assert json_data["message"] == "UserRoles deleted successfully"

def test_Resource(client, jwt_token):
    response = client.get('/api/Resources', headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 200
    
    response = client.post('/api/Resources', json={
        'name': 'test',
        'typeId': 1,
        'info': '{"x":"test", "y":"test", "z":"test"}'
    }, headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 201 
    json_data = response.get_json()
    
    assert "message" in json_data
    assert "resourceId" in json_data
    assert isinstance(json_data["resourceId"], int)
    assert json_data["resourceId"] > 0
    assert json_data["message"] == "entry added"
    
    resourceId = json_data["resourceId"]
    response = client.put(f'/api/Resources/{resourceId}', json={
        'name': 'takanashi kiara',
        'typeId': 1,
        'info': '{"x": "k", "y": "f", "z": "p"}'
    }, headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "resourceId" in json_data
    assert "message" in json_data
    assert isinstance(json_data["resourceId"], int)
    assert json_data["resourceId"] > 0
    assert json_data["message"] == "update successful"
    
    resourceId = json_data["resourceId"]
    response = client.delete(f'/api/Resources/{resourceId}', headers={"Authorization": f"Bearer {jwt_token}"})
    
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "resourceId" in json_data
    assert "message" in json_data
    assert isinstance(json_data["resourceId"], int)
    assert json_data["resourceId"] > 0
    assert json_data["message"] == "Resources deleted successfully"

def test_ResourceTypes(client, jwt_token):
    response = client.get('/api/ResourceTypes', headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 200
    
    response = client.post('/api/ResourceTypes', json={
        "typeName": "testName"
    }, headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 201 
    json_data = response.get_json()
    
    assert "message" in json_data
    assert "typeId" in json_data
    assert isinstance(json_data["typeId"], int)
    assert json_data["typeId"] > 0
    assert json_data["message"] == "entry added"
    
    typeId = json_data["typeId"]
    response = client.put(f'/api/ResourceTypes/{typeId}', json={
        "typeName": "deadbeat",
    }, headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "typeId" in json_data
    assert "message" in json_data
    assert isinstance(json_data["typeId"], int)
    assert json_data["typeId"] > 0
    assert json_data["message"] == "update successful"
    
    typeId = json_data["typeId"]
    response = client.delete(f'/api/ResourceTypes/{typeId}', headers={"Authorization": f"Bearer {jwt_token}"})
    
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "typeId" in json_data
    assert "message" in json_data
    assert isinstance(json_data["typeId"], int)
    assert json_data["typeId"] > 0
    assert json_data["message"] == "ResourceTypes deleted successfully"

def test_ScheduledWork(client, jwt_token):
    response = client.get('/api/ScheduledWork', headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 200
    
    response = client.post('/api/ScheduledWork', json={
        'userId': 1,
        'fromDate': '2024-03-05',
        'duration': '00:00:00'
    }, headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 201 
   
    json_data = response.get_json()
    
    assert "message" in json_data
    assert "workId" in json_data
    assert isinstance(json_data["workId"], int)
    assert json_data["workId"] > 0
    assert json_data["message"] == "entry added"
    
    workId = json_data["workId"]
    response = client.put(f'/api/ScheduledWork/{workId}', json={
        "userId": "1",
        "fromDate": "2025-10-20",
        "duration": "12:00:00"
    }, headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "workId" in json_data
    assert "message" in json_data
    assert isinstance(json_data["workId"], int)
    assert json_data["workId"] > 0
    assert json_data["message"] == "update successful"
    
    workId = json_data["workId"]
    response = client.delete(f'/api/ScheduledWork/{workId}', headers={"Authorization": f"Bearer {jwt_token}"})
    
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "workId" in json_data
    assert "message" in json_data
    assert isinstance(json_data["workId"], int)
    assert json_data["workId"] > 0
    assert json_data["message"] == "ScheduledWork deleted successfully"

def test_ScheduledMaintenance(client, jwt_token):
    response = client.get('/api/ScheduledMaintenance', headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 200
    
    response = client.post('/api/ScheduledMaintenance', json={
        'userId': 1,
        'fromDate': '2024-03-05',
        'duration': '00:00:00',
        'description': 'test',
        'maintenancetypeid': 1
    }, headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 201 
   
    json_data = response.get_json()
    
    assert "message" in json_data
    assert "maintId" in json_data
    assert isinstance(json_data["maintId"], int)
    assert json_data["maintId"] > 0
    assert json_data["message"] == "entry added"
    
    maintId = json_data["maintId"]
    response = client.put(f'/api/ScheduledMaintenance/{maintId}', json={
        "userId": "1",
        "fromDate": "2025-10-20",
        "duration": "12:00:00",
        'description': 'test',
        'maintenancetypeid': 1
    }, headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "maintId" in json_data
    assert "message" in json_data
    assert isinstance(json_data["maintId"], int)
    assert json_data["maintId"] > 0
    assert json_data["message"] == "update successful"
    
    maintId = json_data["maintId"]
    response = client.delete(f'/api/ScheduledMaintenance/{maintId}', headers={"Authorization": f"Bearer {jwt_token}"})
    
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "maintId" in json_data
    assert "message" in json_data
    assert isinstance(json_data["maintId"], int)
    assert json_data["maintId"] > 0
    assert json_data["message"] == "ScheduledMaintenance deleted successfully"

def test_ScheduledResources(client, jwt_token):
    response = client.get('/api/ScheduledResources', headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 200
    
    # Start Temporary POST
    response = client.post('/api/ScheduledWork', json={
        'userId': 1,
        'fromDate': '2030-10-20',
        'duration': '24:00:00'
    }, headers={"Authorization": f"Bearer {jwt_token}"})
    json_data = response.get_json()
    workId_temp = json_data["workId"]
    
    response = client.post('/api/Resources', json={
        'name': 'test',
        'typeId': 1,
        'info': '{"x":"test", "y":"test", "z":"test"}'
    }, headers={"Authorization": f"Bearer {jwt_token}"})
    json_data = response.get_json()
    resourceId_temp = json_data["resourceId"]
    # End Temporary POST
    
    response = client.post('/api/ScheduledResources', json={
        'workId': workId_temp,
        'resourceId': resourceId_temp
    }, headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 201 
   
    json_data = response.get_json()
    
    assert "message" in json_data
    assert "workId" in json_data
    assert "resourceId" in json_data
    assert isinstance(json_data["workId"], int)
    assert isinstance(json_data["resourceId"], int)
    assert json_data["workId"] > 0
    assert json_data["resourceId"] > 0
    assert json_data["message"] == "entry added"
    
    workId = json_data["workId"]
    resourceId = json_data["resourceId"]
    
    response = client.put(f'/api/ScheduledResources/{workId}/{resourceId}', json={
        'workId': workId_temp,
        'resourceId': resourceId_temp
    }, headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "message" in json_data
    assert "workId" in json_data
    assert "resourceId" in json_data
    assert isinstance(json_data["workId"], int)
    assert isinstance(json_data["resourceId"], int)
    assert json_data["workId"] > 0
    assert json_data["resourceId"] > 0
    assert json_data["message"] == "update successful"
    
    workId = json_data["workId"]
    resourceId = json_data["resourceId"]
    response = client.delete(f'/api/ScheduledResources/{workId}/{resourceId}', headers={"Authorization": f"Bearer {jwt_token}"})
    
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "message" in json_data
    assert "workId" in json_data
    assert "resourceId" in json_data
    assert isinstance(json_data["workId"], int)
    assert isinstance(json_data["resourceId"], int)
    assert json_data["workId"] > 0
    assert json_data["resourceId"] > 0
    assert json_data["message"] == "ScheduledResources deleted successfully"
    
    # Start Temporary DELETE
    client.delete(f'/api/ScheduledWork/{workId_temp}', headers={"Authorization": f"Bearer {jwt_token}"})
    client.delete(f'/api/Resources/{resourceId_temp}', headers={"Authorization": f"Bearer {jwt_token}"})
    # End Temporary DELETE

def test_MaintanedResources(client, jwt_token):
    response = client.get('/api/MaintanedResources', headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 200
    
    # Start Temporary POST
    response = client.post('/api/ScheduledMaintenance', json={
        'userId': 1,
        'fromDate': '2030-10-20',
        'duration': '00:00:00',
        'description': 'test',
        'maintenancetypeid': 1
    }, headers={"Authorization": f"Bearer {jwt_token}"})
    json_data = response.get_json()
    maintId_temp = json_data["maintId"]
    
    response = client.post('/api/Resources', json={
        'name': 'test',
        'typeId': 1,
        'info': '{"x":"test", "y":"test", "z":"test"}'
    }, headers={"Authorization": f"Bearer {jwt_token}"})
    json_data = response.get_json()
    resourceId_temp = json_data["resourceId"]
    # End Temporary POST
    
    response = client.post('/api/MaintanedResources', json={
        'maintId': maintId_temp,
        'resourceId': resourceId_temp
    }, headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 201 
   
    json_data = response.get_json()
    
    assert "message" in json_data
    assert "maintId" in json_data
    assert "resourceId" in json_data
    assert isinstance(json_data["maintId"], int)
    assert isinstance(json_data["resourceId"], int)
    assert json_data["maintId"] > 0
    assert json_data["resourceId"] > 0
    assert json_data["message"] == "entry added"
    
    maintId = json_data["maintId"]
    resourceId = json_data["resourceId"]
    
    response = client.put(f'/api/MaintanedResources/{maintId}/{resourceId}', json={
        'maintId': maintId_temp,
        'resourceId': resourceId_temp
    }, headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "message" in json_data
    assert "maintId" in json_data
    assert "resourceId" in json_data
    assert isinstance(json_data["maintId"], int)
    assert isinstance(json_data["resourceId"], int)
    assert json_data["maintId"] > 0
    assert json_data["resourceId"] > 0
    assert json_data["message"] == "update successful"
    
    maintId = json_data["maintId"]
    resourceId = json_data["resourceId"]
    response = client.delete(f'/api/MaintanedResources/{maintId}/{resourceId}', headers={"Authorization": f"Bearer {jwt_token}"})
    
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "message" in json_data
    assert "maintId" in json_data
    assert "resourceId" in json_data
    assert isinstance(json_data["maintId"], int)
    assert isinstance(json_data["resourceId"], int)
    assert json_data["maintId"] > 0
    assert json_data["resourceId"] > 0
    assert json_data["message"] == "MaintanedResources deleted successfully"
    
    # Start Temporary DELETE
    client.delete(f'/api/ScheduledMaintenance/{maintId_temp}', headers={"Authorization": f"Bearer {jwt_token}"})
    client.delete(f'/api/Resources/{resourceId_temp}', headers={"Authorization": f"Bearer {jwt_token}"})
    # End Temporary DELETE

def test_inserWork(client, jwt_token):
    response = client.post('/api/insertWork', json={
        "resourceId": 1,
        "userId": 1,
        "fromDate": "2030-10-20",
        "duration": "24:00:00"
    }, headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 201
    json_data = response.get_json()
    
    assert "message" in json_data
    assert "workId" in json_data
    assert "resourceId" in json_data
    assert isinstance(json_data["workId"], int)
    assert isinstance(json_data["resourceId"], int)
    assert json_data["workId"] > 0
    assert json_data["resourceId"] > 0
    assert json_data["message"] == "entry added"
    
    # DELETE
    client.delete(f'/api/ScheduledResources/{json_data["workId"]}/{json_data["resourceId"]}', headers={"Authorization": f"Bearer {jwt_token}"})
    client.delete(f'/api/ScheduledWork/{json_data["workId"]}', headers={"Authorization": f"Bearer {jwt_token}"})

def test_insertMaintenance(client, jwt_token):
    # POST TEST
    response = client.post('/api/insertMaintenance', json={
        "resourceId": 1,
        "userId": 1,
        "fromDate": "2030-10-20",
        "duration": "24:00:00",
        "description": "test",
        "maintenancetypeid": 1
    }, headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 201
    json_data = response.get_json()
    
    assert "message" in json_data
    assert "maintId" in json_data
    assert "resourceId" in json_data
    assert isinstance(json_data["maintId"], int)
    assert isinstance(json_data["resourceId"], int)
    assert json_data["maintId"] > 0
    assert json_data["resourceId"] > 0
    assert json_data["message"] == "entry added"
    
    # DELETE
    client.delete(f'/api/MaintanedResources/{json_data["maintId"]}/{json_data["resourceId"]}', headers={"Authorization": f"Bearer {jwt_token}"})
    client.delete(f'/api/ScheduledMaintenance/{json_data["maintId"]}', headers={"Authorization": f"Bearer {jwt_token}"})

def test_checkAvailability(client, jwt_token):
    response = client.get('/api/checkAvailability/1?date=2024-10-08T11:00:00&interval=00:30:00', headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 200
    json_data = response.get_json()
    assert "message" in json_data
    assert isinstance(json_data["message"], bool)

def test_maintenanceType(client, jwt_token):
    # GET TEST
    response = client.get('/api/MaintenanceType', headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 200
    
    # POST TEST
    response = client.post('/api/MaintenanceType', json={
        "typeName": "testType",
    }, headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 201 
    json_data = response.get_json()
    
    assert "message" in json_data
    assert "maintenanceTypeId" in json_data
    assert isinstance(json_data["maintenanceTypeId"], int)
    assert json_data["maintenanceTypeId"] > 0
    assert json_data["message"] == "entry added"
    
    # PUT TEST
    maintenanceTypeId = json_data["maintenanceTypeId"]
    response = client.put(f'/api/MaintenanceType/{maintenanceTypeId}', json={
        "typeName": "sigma",
    }, headers={"Authorization": f"Bearer {jwt_token}"})
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "maintenanceTypeId" in json_data
    assert "message" in json_data
    assert isinstance(json_data["maintenanceTypeId"], int)
    assert json_data["maintenanceTypeId"] > 0
    assert json_data["message"] == "update successful"
    
    # DELETE TEST
    maintenanceTypeId = json_data["maintenanceTypeId"]
    response = client.delete(f'/api/MaintenanceType/{maintenanceTypeId}', headers={"Authorization": f"Bearer {jwt_token}"})
    
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "maintenanceTypeId" in json_data
    assert "message" in json_data
    assert isinstance(json_data["maintenanceTypeId"], int)
    assert json_data["maintenanceTypeId"] > 0
    assert json_data["message"] == "maintenanceType deleted successfully"

def test_login(client):
    credentials = {
        "email": "kristof20011020@gmail.com",
        "password": "lenin17@"
    }
        
    response = client.post('/api/login', json=credentials)
    assert response.status_code == 200 
        
    json_data = response.get_json()
        
    assert "email" in json_data
    assert "message" in json_data
    assert "token" in json_data
    assert "userId" in json_data
        
    assert json_data["email"] == "kristof20011020@gmail.com"
    assert json_data["message"] == "Login successful"
    assert isinstance(json_data["token"], str)
    assert json_data["token"] != "" 
    assert isinstance(json_data["userId"], int)
    assert json_data["userId"] > 0
