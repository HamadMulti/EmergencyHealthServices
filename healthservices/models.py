from django.db import models
from django.utils import timezone

class Patient(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_images/', default='', blank=True)
    location = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_accepted = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)  

    def __str__(self):
        return f"Patient: {self.username}"

class AmbulanceDriver(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_images/', default='profile_images/ambulance_driver.png', blank=True)
    location = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=False)  # New field added

    def __str__(self):
        return f"Ambulance Driver: {self.username}"

class AdminStaff(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_images/', default='profile_images/admin.png', blank=True)

    def __str__(self):
        return f"Admin: {self.username}"
