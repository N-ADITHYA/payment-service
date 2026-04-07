from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_order():
    response = client.post("/create_order", json={"amount": 100})

    assert response.status_code == 200

    data = response.json()

    assert "order_id" in data
    assert data["status"] == "Created"

def test_pay_current_order():
    response = client.post("/create_order", json={"amount": 300})
    order_id = response.json()["order_id"]

    pay = client.post("/pay", json={"curr_id": order_id, "payment": 300})

    assert pay.status_code == 200

    data = pay.json()

    assert "order_id" in data
    assert data["status"] == "Completed"
    assert data["remaining"] == 0

def test_half_payment():
    response = client.post("/create_order", json={"amount": 120})
    order_id = response.json()["order_id"]

    data = response.json()

    assert "order_id" in data

    pay = client.post("/pay", json={"curr_id": order_id, "payment": 100})

    assert pay.status_code == 200
    assert pay.json()["status"] == "Pending"

def test_edge_cases():
    response = client.post("/create_order", json={"amount": 120})
    order_id = response.json()["order_id"]

    pay = client.post("/pay", json={"curr_id": order_id, "payment": 121})

    assert pay.status_code == 400

