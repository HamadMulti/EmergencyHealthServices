from django.test import TestCase, Client
from django.urls import reverse
from .models import Patient, AmbulanceDriver, AdminStaff

class AuthenticationTests(TestCase):
    
    def test_patient_signup_success(self):
        """Test successful patient signup"""
        client = Client()
        response = client.post(reverse("signup"), {
            "username": "testpatient",
            "email": "patient@test.com",
            "password": "StrongPass1!",
            "role": "patient",
            "location": "Test City"
        })
        # Should redirect to signin after successful signup
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Patient.objects.filter(email="patient@test.com").exists())

    def test_signup_with_existing_email(self):
        """Test signup with duplicate email"""
        Patient.objects.create(username="abc", email="existing@test.com", password="StrongPass1!", location="City")
        
        client = Client()
        response = client.post(reverse("signup"), {
            "username": "newuser",
            "email": "existing@test.com",
            "password": "StrongPass1!",
            "role": "patient",
            "location": "New City"
        })
        
        # Expect email already exists alert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Patient.objects.filter(email="existing@test.com").count(), 1)

    def test_signin_patient_success(self):
        """Test successful patient signin"""
        Patient.objects.create(username="abc", email="login@test.com", password="StrongPass1!", location="City")
        
        client = Client()
        response = client.post(reverse("signin"), {
            "email": "login@test.com",
            "password": "StrongPass1!",
        })
        
        # Should redirect to home
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("home"))

    def test_signin_invalid_credentials(self):
        """Test signin with wrong credentials"""
        client = Client()
        response = client.post(reverse("signin"), {
            "email": "wrong@test.com",
            "password": "WrongPass!",
        })
        
        # Should redirect back to signin
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("signin"))