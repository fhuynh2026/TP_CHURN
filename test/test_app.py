
import json
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# ✅ Test page d'accueil
def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Churn' in response.data

# ✅ Test prédiction valide
def test_prediction_valid(client):
    data = {
        "Age": 40,
        "Account_Manager": 1,
        "Years": 5,
        "Num_Sites": 10
    }

    response = client.post(
        '/predict',
        data=json.dumps(data),
        content_type='application/json'
    )

    assert response.status_code == 200

    json_data = response.get_json()
    assert 'prediction' in json_data
    assert 'probability' in json_data

# ✅ Test valeurs invalides
def test_prediction_invalid(client):
    data = {
        "Age": "invalid",
        "Account_Manager": 1,
        "Years": 5,
        "Num_Sites": 10
    }

    response = client.post(
        '/predict',
        data=json.dumps(data),
        content_type='application/json'
    )

    assert response.status_code == 200
    json_data = response.get_json()
    assert 'error' in json_data

# ✅ Test champ manquant
def test_missing_field(client):
    data = {
        "Age": 40,
        "Years": 5,
        "Num_Sites": 10
    }

    response = client.post(
        '/predict',
        data=json.dumps(data),
        content_type='application/json'
    )

    json_data = response.get_json()
    assert 'error' in json_data