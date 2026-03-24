# test_app.py
import pytest
from app import app  # Import your Flask/FastAPI app or main functions

def test_app_exists():
    """Test that the app exists"""
    assert app is not None

def test_home_page():
    """Test the home page endpoint"""
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200

# Add more tests as needed