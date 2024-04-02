# your_app/admin.py
from django.contrib import admin
from .models import UserProfile, HeartDiseasePredictionData, DiabetesPredictionData, ContactMessage

admin.site.register(UserProfile)
admin.site.register(HeartDiseasePredictionData)
admin.site.register(DiabetesPredictionData)
admin.site.register(ContactMessage)

