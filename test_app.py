import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_userData(client):
    # GET TEST
    response = client.get('/api/UserData')
    assert response.status_code == 200
    
    # POST TEST
    response = client.post('/api/UserData', json={
        "email": "testemail@test.com",
        "firstName": "test",
        "lastName": "test",
        "password": "password",
        "roleId": 1
    })
    assert response.status_code == 201 
    json_data = response.get_json()
    
    assert "message" in json_data
    assert "userId" in json_data
    assert isinstance(json_data["userId"], int)
    assert json_data["userId"] > 0
    assert json_data["message"] == "entry added"
    
    #PUT TEST
    userId = json_data["userId"]
    response = client.put(f'/api/UserData/{userId}', json={
        "email": "edit@edit.com",
        "firstName": "edit",
        "lastName": "edit",
        "password": "edit",
        "roleId": 1
    })
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "userId" in json_data
    assert "message" in json_data
    assert isinstance(json_data["userId"], int)
    assert json_data["userId"] > 0
    assert json_data["message"] == "update successfull"
    
    # DELETE TEST
    userId = json_data["userId"]
    response = client.delete(f'/api/UserData/{userId}')
    
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "userId" in json_data
    assert "message" in json_data
    assert isinstance(json_data["userId"], int)
    assert json_data["userId"] > 0
    assert json_data["message"] == "userData deleted successfully"

def test_userRoles(client):
    # GET TEST
    response = client.get('/api/UserRoles')
    assert response.status_code == 200
    
    # POST TEST
    response = client.post('/api/UserRoles', json={
        "roleName": "testRole",
    })
    assert response.status_code == 201 
    json_data = response.get_json()
    
    assert "message" in json_data
    assert "roleId" in json_data
    assert isinstance(json_data["roleId"], int)
    assert json_data["roleId"] > 0
    assert json_data["message"] == "entry added"
    
    #PUT TEST
    roleId = json_data["roleId"]
    response = client.put(f'/api/UserRoles/{roleId}', json={
        "roleName": "deadbeat",
    })
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "roleId" in json_data
    assert "message" in json_data
    assert isinstance(json_data["roleId"], int)
    assert json_data["roleId"] > 0
    assert json_data["message"] == "update successfull"
    
    # DELETE TEST
    roleId = json_data["roleId"]
    response = client.delete(f'/api/UserRoles/{roleId}')
    
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "roleId" in json_data
    assert "message" in json_data
    assert isinstance(json_data["roleId"], int)
    assert json_data["roleId"] > 0
    assert json_data["message"] == "UserRoles deleted successfully"

def test_Resource(client):
    # GET TEST
    response = client.get('/api/Resources')
    assert response.status_code == 200
    
    # POST TEST
    response = client.post('/api/Resources', json={
    'name': 'test',
    'typeId': 1,
    'info': '{"x":"test", "y":"test", "z":"test"}'
    })
    assert response.status_code == 201 
    json_data = response.get_json()
    
    assert "message" in json_data
    assert "resourceId" in json_data
    assert isinstance(json_data["resourceId"], int)
    assert json_data["resourceId"] > 0
    assert json_data["message"] == "entry added"
    
    #PUT TEST
    resourceId = json_data["resourceId"]
    response = client.put(f'/api/Resources/{resourceId}', json={
        'name': 'takanashi kiara',
        'typeId': 1,
        'info': '{"x": "k", "y": "f", "z": "p"}'
    })
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "resourceId" in json_data
    assert "message" in json_data
    assert isinstance(json_data["resourceId"], int)
    assert json_data["resourceId"] > 0
    assert json_data["message"] == "update successfull"
    
    # DELETE TEST
    resourceId = json_data["resourceId"]
    response = client.delete(f'/api/Resources/{resourceId}')
    
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "resourceId" in json_data
    assert "message" in json_data
    assert isinstance(json_data["resourceId"], int)
    assert json_data["resourceId"] > 0
    assert json_data["message"] == "Resources deleted successfully"
    
def test_ResourceTypes(client):
    # GET TEST
    response = client.get('/api/ResourceTypes')
    assert response.status_code == 200
    
    # POST TEST
    response = client.post('/api/ResourceTypes', json={
        "typeName": "testName"
    })
    assert response.status_code == 201 
    json_data = response.get_json()
    
    assert "message" in json_data
    assert "typeId" in json_data
    assert isinstance(json_data["typeId"], int)
    assert json_data["typeId"] > 0
    assert json_data["message"] == "entry added"
    
    #PUT TEST
    typeId = json_data["typeId"]
    response = client.put(f'/api/ResourceTypes/{typeId}', json={
        "typeName": "deadbeat",
    })
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "typeId" in json_data
    assert "message" in json_data
    assert isinstance(json_data["typeId"], int)
    assert json_data["typeId"] > 0
    assert json_data["message"] == "update successfull"
    
    # DELETE TEST
    typeId = json_data["typeId"]
    response = client.delete(f'/api/ResourceTypes/{typeId}')
    
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "typeId" in json_data
    assert "message" in json_data
    assert isinstance(json_data["typeId"], int)
    assert json_data["typeId"] > 0
    assert json_data["message"] == "ResourceTypes deleted successfully"
    
def test_ScheduledWork(client):
    # GET TEST
    response = client.get('/api/ScheduledWork')
    assert response.status_code == 200
    
    # POST TEST
    response = client.post('/api/ScheduledWork', json={
        'userId': 1,
        'fromDate': '2024-03-05',
        'duration': '00:00:00'
    })
    assert response.status_code == 201 
   
    json_data = response.get_json()
    
    assert "message" in json_data
    assert "workId" in json_data
    assert isinstance(json_data["workId"], int)
    assert json_data["workId"] > 0
    assert json_data["message"] == "entry added"
    
    
    #PUT TEST
    workId = json_data["workId"]
    response = client.put(f'/api/ScheduledWork/{workId}', json={
        "userId": "1",
        "fromDate": "2025-10-20",
        "duration": "12:00:00"
    })
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "workId" in json_data
    assert "message" in json_data
    assert isinstance(json_data["workId"], int)
    assert json_data["workId"] > 0
    assert json_data["message"] == "update successfull"
    
    # DELETE TEST
    workId = json_data["workId"]
    response = client.delete(f'/api/ScheduledWork/{workId}')
    
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "workId" in json_data
    assert "message" in json_data
    assert isinstance(json_data["workId"], int)
    assert json_data["workId"] > 0
    assert json_data["message"] == "ScheduledWork deleted successfully"

def test_ScheduledMaintenance(client):
    # GET TEST
    response = client.get('/api/ScheduledMaintenance')
    assert response.status_code == 200
    
    # POST TEST
    response = client.post('/api/ScheduledMaintenance', json={
        'userId': 1,
        'fromDate': '2024-03-05',
        'duration': '00:00:00',
        'description': 'test',
        'maintenancetypeid': 1
    })
    assert response.status_code == 201 
   
    json_data = response.get_json()
    
    assert "message" in json_data
    assert "maintId" in json_data
    assert isinstance(json_data["maintId"], int)
    assert json_data["maintId"] > 0
    assert json_data["message"] == "entry added"
    
    
    #PUT TEST
    maintId = json_data["maintId"]
    response = client.put(f'/api/ScheduledMaintenance/{maintId}', json={
        "userId": "1",
        "fromDate": "2025-10-20",
        "duration": "12:00:00",
        'description': 'test',
        'maintenancetypeid': 1
    })
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "maintId" in json_data
    assert "message" in json_data
    assert isinstance(json_data["maintId"], int)
    assert json_data["maintId"] > 0
    assert json_data["message"] == "update successfull"
    
    # DELETE TEST
    maintId = json_data["maintId"]
    response = client.delete(f'/api/ScheduledMaintenance/{maintId}')
    
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "maintId" in json_data
    assert "message" in json_data
    assert isinstance(json_data["maintId"], int)
    assert json_data["maintId"] > 0
    assert json_data["message"] == "ScheduledMaintenance deleted successfully"
    
def test_ScheduledResources(client):
    # GET TEST
    response = client.get('/api/ScheduledResources')
    assert response.status_code == 200
    
    # POST TEST
    # START TEMP POST
    response = client.post('/api/ScheduledWork', json={
        'userId': 1,
        'fromDate': '2030-10-20',
        'duration': '24:00:00'
    })
    json_data = response.get_json()
    workId_temp = json_data["workId"]
    
    response = client.post('/api/Resources', json={
    'name': 'test',
    'typeId': 1,
    'info': '{"x":"test", "y":"test", "z":"test"}'
    })
    json_data = response.get_json()
    resourceId_temp = json_data["resourceId"]
    # END
    
    response = client.post('/api/ScheduledResources', json={
        'workId': workId_temp,
        'resourceId': resourceId_temp
    })
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
    
    
    #PUT TEST
    workId = json_data["workId"]
    resourceId = json_data["resourceId"]
    
    response = client.put(f'/api/ScheduledResources/{workId}/{resourceId}', json={
        'workId': workId_temp,
        'resourceId': resourceId_temp
    })
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "message" in json_data
    assert "workId" in json_data
    assert "resourceId" in json_data
    assert isinstance(json_data["workId"], int)
    assert isinstance(json_data["resourceId"], int)
    assert json_data["workId"] > 0
    assert json_data["resourceId"] > 0
    assert json_data["message"] == "update successfull"
    
    # DELETE TEST
    workId = json_data["workId"]
    resourceId = json_data["resourceId"]
    response = client.delete(f'/api/ScheduledResources/{workId}/{resourceId}')
    
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
    
    # START TEMP DELETE
    client.delete(f'/api/ScheduledWork/{workId_temp}')
    client.delete(f'/api/Resources/{resourceId_temp}')
    
    # END
    
def test_MaintanedResources(client):
    # GET TEST
    response = client.get('/api/MaintanedResources')
    assert response.status_code == 200
    
    # POST TEST
    # START TEMP POST
    response = client.post('/api/ScheduledMaintenance', json={
        'userId': 1,
        'fromDate': '2030-10-20',
        'duration': '00:00:00',
        'description': 'test',
        'maintenancetypeid': 1
    })
    json_data = response.get_json()
    maintId_temp = json_data["maintId"]
    
    response = client.post('/api/Resources', json={
    'name': 'test',
    'typeId': 1,
    'info': '{"x":"test", "y":"test", "z":"test"}'
    })
    json_data = response.get_json()
    resourceId_temp = json_data["resourceId"]
    # END
    
    response = client.post('/api/MaintanedResources', json={
        'maintId': maintId_temp,
        'resourceId': resourceId_temp
    })
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
    
    
    #PUT TEST
    maintId = json_data["maintId"]
    resourceId = json_data["resourceId"]
    
    response = client.put(f'/api/MaintanedResources/{maintId}/{resourceId}', json={
        'maintId': maintId_temp,
        'resourceId': resourceId_temp
    })
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert "message" in json_data
    assert "maintId" in json_data
    assert "resourceId" in json_data
    assert isinstance(json_data["maintId"], int)
    assert isinstance(json_data["resourceId"], int)
    assert json_data["maintId"] > 0
    assert json_data["resourceId"] > 0
    assert json_data["message"] == "update successfull"
    
    # DELETE TEST
    maintId = json_data["maintId"]
    resourceId = json_data["resourceId"]
    response = client.delete(f'/api/MaintanedResources/{maintId}/{resourceId}')
    
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
    
    # START TEMP DELETE
    client.delete(f'/api/ScheduledMaintenance/{maintId_temp}')
    client.delete(f'/api/Resources/{resourceId_temp}')

    # END

def test_inserWork(client):
    #POST TEST
    response = client.post('/api/insertWork', json={
        "resourceId": 1,
        "userId": 1,
        "fromDate": "2030-10-20",
        "duration": "24:00:00"
})
    assert response.status_code == 201
    json_data = response.get_json()
    print(json_data)
    
    assert "message" in json_data
    assert "workId" in json_data
    assert "resourceId" in json_data
    assert isinstance(json_data["workId"], int)
    assert isinstance(json_data["resourceId"], int)
    assert json_data["workId"] > 0
    assert json_data["resourceId"] > 0
    assert json_data["message"] == "entry added"
    
    #DELETE
    client.delete(f'/api/ScheduledResources/{json_data["workId"]}/{json_data["resourceId"]}')
    client.delete(f'/api/ScheduledWork/{json_data["workId"]}')
    
    #END

def test_insertMaintenance(client):
    #POST TEST
    response = client.post('/api/insertMaintenance', json={
        "resourceId": 1,
        "userId": 1,
        "fromDate": "2030-10-20",
        "duration": "24:00:00",
        "description": "test",
        "maintenancetypeid": 1
    })
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
    
    #DELETE
    client.delete(f'/api/MaintanedResources/{json_data["maintId"]}/{json_data["resourceId"]}')
    client.delete(f'/api/ScheduledMaintenance/{json_data["maintId"]}')
    
    #END
    
def test_checkAvailability(client):
    response = client.get('/api/checkAvailability/1?date=2024-10-08T11:00:00&interval=00:30:00')
    assert response.status_code == 200
    json_data = response.get_json()
    assert "message" in json_data
    assert isinstance(json_data["message"], bool)
    