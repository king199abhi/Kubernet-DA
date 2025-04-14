import pytest
from app import app  # Import your Flask app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home route"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

def test_health_check(client):
    """Test the health route"""
    response = client.get('/health')
    assert response.status_code == 200
    assert b"healthy" in response.data
    
