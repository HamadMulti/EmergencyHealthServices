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
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Ambulance Driver: {self.username}"

class AdminStaff(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_images/', default='profile_images/admin.png', blank=True)

    def __str__(self):
        return f"Admin: {self.username}"

class AmbulanceRegistrartionForm(models.Model):
    patient_email = models.CharField(max_length=100) 
    driver_email = models.CharField(max_length=100, blank=True, null=True)   
    patient_current_location = models.CharField(max_length=100)
    patient_phone_number = models.CharField(max_length=100)
    patient_emergency_condition = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.patient_current_location} - {self.patient_emergency_condition}"
    
class Notifications(models.Model):
    patient_email = models.CharField(max_length=100) 
    driver_email = models.CharField(max_length=100, blank=True, null=True)   
    message = models.CharField(max_length=255)   
    date_and_time = models.DateTimeField(default=timezone.now)  

    def __str__(self):
        return f"Notification for {self.patient_email} from {self.driver_email or 'System'}"
