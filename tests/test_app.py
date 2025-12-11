import pytest
from main import app # import flask app to test

@pytest.fixture
def client(): # Fixture: sets up a fake browser for tests (no real server)
    app.config['TESTING'] = True # enables test mode (no errors on bad routes)
    with app.test_client() as client: # create test client
        yield client # hands it to the test, cleans up after
        
def test_hello_endpoint(client):
    """Tests the root route returns 200 OK and full message"""
    response = client.get('/') # simulate GET request to root route
    assert response.status_code == 200 # check for 200 OK
    assert "Docker rocks - next: SpaceX RAG! 🌌" in response.get_data(as_text=True) # Text mode = emoji OK
    
def test_hello_contains_emoji(client):
    """Bonus test: Verifies galaxy emoji is there"""
    response = client.get('/')
    assert "🌌" in response.get_data(as_text=True) # specific substring check