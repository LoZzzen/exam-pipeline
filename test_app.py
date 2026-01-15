import pytest
from unittest.mock import MagicMock, patch
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    """Test endpoint /health"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json()['status'] == 'healthy'

def test_add_item_success(client):
    """Test ajout d'un item valide"""
    with patch('app.cache') as mock_cache:
        mock_cache.incr = MagicMock()
        response = client.post('/items', json={"name": "Clavier", "quantity": 5})
        assert response.status_code == 201
        assert response.get_json()['name'] == 'Clavier'

def test_add_item_missing_name(client):
    """Test erreur quand name manquant"""
    response = client.post('/items', json={"quantity": 5})
    assert response.status_code == 400

def test_get_items(client):
    """Test récupération des items"""
    response = client.get('/items')
    assert response.status_code == 200
    assert 'items' in response.get_json()
