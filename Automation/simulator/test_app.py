import pytest
from app import app

@pytest.fixture
def client():
    app.config['Testing']=True
    with app.test_client() as client:
        yield client
        
def test_get_equipment(client):
    response = client.get("/api/equipment")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) ==3
    # [{"id":101,"name":"Flight","status":"Operational","type":"FCU"},
    #  {"id":102,"name":"Navigational System","status":"Operational","type":"NS"}]
    assert data[0]["id"] == 101
    assert data[0]["name"] == "flight control unit"
    assert data[0]["status"] == "operational"
    assert data[0]["type"] == "fcu"

def test_get_equipment_id(client):
    id=102
    response = client.get("/api/equipment/102")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, dict)
    assert len(data) ==4
    # [{"id":101,"name":"Flight","status":"Operational","type":"FCU"},
    #  {"id":102,"name":"Navigational System","status":"Operational","type":"NS"}]
    assert data["id"] == 102
    assert data["name"] == "navigation system"
    assert data["status"] == "operational"
    assert data["type"] == "NS"