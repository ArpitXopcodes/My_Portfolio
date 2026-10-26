"""
Tests for Arpit's Portfolio Website
Run with: pytest test_app.py -v
"""

import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_homepage(client):
    """Test that homepage loads successfully"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Arpit Turukmare" in response.data


def test_projects_page(client):
    """Test that projects page loads and shows project names"""
    response = client.get("/projects")
    assert response.status_code == 200
    assert b"TechSentry" in response.data
    assert b"ScoreScope-AI" in response.data


def test_skills_page(client):
    """Test that skills page loads and shows skills"""
    response = client.get("/skills")
    assert response.status_code == 200
    assert b"Python" in response.data
    assert b"Machine Learning" in response.data


def test_achievements_page(client):
    """Test that achievements page loads"""
    response = client.get("/achievements")
    assert response.status_code == 200
    assert b"AXION" in response.data
    assert b"Innovation Challenge" in response.data


def test_health_endpoint(client):
    """Test that health endpoint returns healthy status"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"


def test_navigation_links(client):
    """Test that navigation links are present on homepage"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"/projects" in response.data
    assert b"/skills" in response.data
    assert b"/achievements" in response.data
