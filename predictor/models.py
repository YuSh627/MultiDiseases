
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError

    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields for user profile if needed
    age = models.IntegerField(default=0)  

    def __str__(self):
        return self.user.username
    


class HeartDiseasePredictionData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    age = models.IntegerField(default=0) 
    sex = models.IntegerField(default=0)
    cp = models.IntegerField(default=0)
    trestbps = models.FloatField(default=0)
    chol = models.FloatField(default=0)
    fbs = models.IntegerField(default=0)
    restecg = models.IntegerField(default=0)
    thalach = models.FloatField(default=0)
    exang = models.IntegerField(default=0)
    oldpeak = models.FloatField(default=0)
    slope = models.IntegerField(default=0)
    ca = models.IntegerField(default=0)
    thal = models.IntegerField(default=0)
    prediction = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return f"{self.user.username} - {self.timestamp}"

class DiabetesPredictionData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    pregnancies = models.IntegerField(default=0)
    glucose = models.IntegerField(default=0)
    blood_pressure = models.IntegerField(default=0)
    skin_thickness = models.IntegerField(default=0)
    insulin = models.IntegerField(default=0)
    bmi = models.FloatField(default=0)
    diabetes_pedigree_function = models.FloatField(default=0)
    age = models.IntegerField(default=0)
    prediction = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.timestamp}"
    
    # contact section
class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.full_name
    