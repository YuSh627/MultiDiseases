from django.urls import path
from . import views
from .views import improve_health, improve_heart, improve_diabetes, diabetes_profile, register, user_login, user_logout, heart_disease_profile, delete_heartdisease_data,delete_diabetes_data,generate_diabetes_chart_data,generate_heartdisease_chart_data


urlpatterns = [
    path('admin/', views.admin_page, name='admin_page'),
    path('profile/', views.profile_page, name='profile_page'),
    path('index/', views.index_page, name='index_page'),
    path('heart/', views.heart_disease_prediction, name='heart_disease_prediction'),
    path('diabetes/', views.diabetes_prediction, name='diabetes_prediction'),
    path('register/', register, name='register'),
    path('', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('heart_disease_profile/', heart_disease_profile, name='heart_disease_profile'),
    path('diabetes_profile/', diabetes_profile, name='diabetes_profile'),
    path('heartdisease/delete/<int:pk>/', delete_heartdisease_data, name='delete_heartdisease_data'),
    path('diabetes/delete/<int:pk>/', delete_diabetes_data, name='delete_diabetes_data'),
    path('generate_diabetes_chart/', generate_diabetes_chart_data, name='generate_diabetes_chart_data'),
    path('generate_heartdisease_chart/', generate_heartdisease_chart_data, name='generate_heartdisease_chart_data'),
    path('improve_health/', improve_health, name='improve_health'),
    

    path('improve_heart/', improve_heart, name='improve_heart'),
    path('improve_diabetes/', improve_diabetes, name='improve_diabetes'),
    
]
