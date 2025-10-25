import pytest
from django.urls import reverse
from django.test import Client
from .models import Patient, AmbulanceDriver, AdminStaff

@pytest.mark.django_db
def test_patient_signup_success():
    client = Client()
    response = client.post(reverse("signup"), {
        "username": "testpatient",
        "email": "patient@test.com",
        "password": "StrongPass1!",
        "role": "patient",
        "location": "Test City"
    })
    # Should redirect to signin after successful signup
    assert response.status_code == 302
    assert Patient.objects.filter(email="patient@test.com").exists()


@pytest.mark.django_db
def test_signup_with_existing_email():
    Patient.objects.create(username="abc", email="existing@test.com", password="StrongPass1!", location="City")

    client = Client()
    response = client.post(reverse("signup"), {
        "username": "newuser",
        "email": "existing@test.com",  # already exists
        "password": "StrongPass1!",
        "role": "patient",
        "location": "New City"
    })

    # Expect email already exists alert (HttpResponse instead of redirect)
    assert response.status_code == 200
    assert Patient.objects.filter(email="existing@test.com").count() == 1


@pytest.mark.django_db
def test_signin_patient_success():
    Patient.objects.create(username="abc", email="login@test.com", password="StrongPass1!", location="City")

    client = Client()
    response = client.post(reverse("signin"), {
        "email": "login@test.com",
        "password": "StrongPass1!",
    })

    # Should redirect to home
    assert response.status_code == 302
    assert response.url == reverse("home")


@pytest.mark.django_db
def test_signin_invalid_credentials():
    client = Client()
    response = client.post(reverse("signin"), {
        "email": "wrong@test.com",
        "password": "WrongPass!",
    })

    # Should redirect back to signin with error message
    assert response.status_code == 302
    assert response.url == reverse("signin")
