import pytest
#from concurrent.futures import ThreadPoolExecutor
import xdist
from app import app
import threading

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


"""def test_get_equipment_concurrently():
    def fetch_equipment(equipment_id):
        with app.test_client() as thread_client:
            response = thread_client.get(f"/api/equipment/{equipment_id}")
            return response.status_code, response.get_json()

    app.config["Testing"] = True
    equipment_ids = [101, 102, 103]

    with ThreadPoolExecutor(max_workers=len(equipment_ids)) as executor:
        responses = list(executor.map(fetch_equipment, equipment_ids))

    assert all(status_code == 200 for status_code, _ in responses)
    assert [data["id"] for _, data in responses] == equipment_ids"""

t1=threading.Thread(target=test_get_equipment)
t2=threading.Thread(target=test_get_equipment_id)
t1.start()
t2.start()
t1.join()
t2.join()