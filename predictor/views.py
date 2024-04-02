from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import HeartDiseasePredictionData, DiabetesPredictionData
from django.utils import timezone
from .forms import ContactForm
import pickle
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from sklearn.preprocessing import StandardScaler
import numpy as np



# Create your views here.

def render_with_base(request, template_name, context=None):
    return render(request, template_name, context)

def render_with_result(request, template_name, context=None):
    return render(request, template_name, context)

def render_with_pmain(request, template_name, context=None):
    return render(request, template_name, context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirect to your home page
    else:
        form = UserCreationForm()
    return render (request, 'registration.html', {'form': form})

    

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect('index_page')  # Redirect to your home page
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid form data.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to your home page


def admin_page(request):
    return render_with_base(request, 'admin.html')

def profile_page(request):
    return render(request, 'profile.html')

def index_page(request):
    return render_with_base(request, 'index.html')

def heart_disease_prediction(request):
    if request.method == 'POST':
        age = float(request.POST.get('age'))
        sex = int(request.POST.get('sex'))
        cp = int(request.POST.get('cp'))
        trestbps = float(request.POST.get('trestbps'))
        chol = float(request.POST.get('chol'))
        fbs = int(request.POST.get('fbs'))
        restecg = int(request.POST.get('restecg'))
        thalach = float(request.POST.get('thalach'))
        exang = int(request.POST.get('exang'))
        oldpeak = float(request.POST.get('oldpeak'))
        slope = int(request.POST.get('slope'))
        ca = int(request.POST.get('ca'))
        thal = int(request.POST.get('thal'))
        features = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
         # Create a feature list
        features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        features = features.reshape(1, -1)
        with open('predictor/heart.pkl', 'rb') as model_file:
            model = pickle.load(model_file)
        
        scaler = StandardScaler()
        with open('predictor/scaler2.pkl', 'rb') as scaler_file:
            scaler = pickle.load(scaler_file)
        features3 = scaler.transform(features)
        # Make a prediction using the trained SVM model
        prediction = model.predict(features3)

        with open('predictor/heart.pkl', 'rb') as model_file:
            model = pickle.load(model_file)
        prediction = model.predict(features)
        timestamp = timezone.now()

        prediction_instance = HeartDiseasePredictionData.objects.create(
            user=request.user,
            age=age,
            sex=sex,
            cp=cp,
            trestbps=trestbps,
            chol=chol,
            fbs=fbs,
            restecg=restecg,
            thalach=thalach,
            exang=exang,
            oldpeak=oldpeak,
            slope=slope,
            ca=ca,
            thal=thal,
            prediction=prediction
        
        )
        prediction_instance.save()

        return render_with_base(request, 'heart_disease_result.html', {'prediction': prediction[0]})

    return render_with_base(request, 'heart_disease_prediction.html')

@login_required

def heart_disease_profile(request):
    
    # Assuming you are trying to retrieve data for the currently logged-in user
    user = request.user

    # Use filter instead of get to handle the case where multiple objects are returned
    prediction_data = HeartDiseasePredictionData.objects.filter(user=user)

    return render_with_pmain(request, 'heart_disease_profile.html', {'prediction_data': prediction_data})

def delete_heartdisease_data(request, pk):
    data_instance = get_object_or_404(HeartDiseasePredictionData, pk=pk)

    # Check if the user making the request is the owner of the data
    if request.user == data_instance.user:
        data_instance.delete()

    return redirect('heart_disease_profile') 

@login_required
def diabetes_prediction(request):
    if request.method == 'POST':
        pregnancies = float(request.POST.get('pregnancies'))
        glucose = float(request.POST.get('glucose'))
        blood_pressure = float(request.POST.get('blood_pressure'))
        skin_thickness = float(request.POST.get('skin_thickness'))
        insulin = float(request.POST.get('insulin'))
        bmi = float(request.POST.get('bmi'))
        diabetes_pedigree_function = float(request.POST.get('diabetes_pedigree_function'))
        age = float(request.POST.get('age'))

        # Create a feature list
        features2 = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])
        features2 = features2.reshape(1, -1)
        with open('predictor/diabetes.pkl', 'rb') as model_file:
            model = pickle.load(model_file)
        
        scaler = StandardScaler()
        with open('predictor/scaler.pkl', 'rb') as scaler_file:
            scaler = pickle.load(scaler_file)
        features3 = scaler.transform(features2)
        # Make a prediction using the trained SVM model
        prediction = model.predict(features3)


        prediction_instance = DiabetesPredictionData.objects.create(
            user=request.user,
            pregnancies=pregnancies,
            glucose=glucose,
            blood_pressure=blood_pressure,
            skin_thickness=skin_thickness,
            insulin=insulin,
            bmi=bmi,
            diabetes_pedigree_function=diabetes_pedigree_function,
            age=age,
            prediction=prediction
        )

        prediction_instance.save()

        return render_with_base(request, 'diabetes_result.html', {'prediction': prediction[0]})

    return render_with_base(request, 'diabetes_prediction.html')
@login_required
def diabetes_profile(request):
    # Assuming you are trying to retrieve data for the currently logged-in user
    user = request.user

    # Use filter instead of get to handle the case where multiple objects are returned
    prediction_data = DiabetesPredictionData.objects.filter(user=user)

    return render_with_pmain(request, 'diabetes_profile.html', {'prediction_data': prediction_data})



def delete_diabetes_data(request, pk):
    data_instance = get_object_or_404(DiabetesPredictionData, pk=pk)

    # Check if the user making the request is the owner of the data
    if request.user == data_instance.user:
        data_instance.delete()

    return redirect('diabetes_profile')


def index_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_page')  # Redirect to the same page after successful submission
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})




def generate_heartdisease_chart_data(request):
    user = request.user
    prediction_data = HeartDiseasePredictionData.objects.filter(user=user)

    # Count the number of negative and positive predictions
    negative_count = 0
    positive_count = 0

    for data in prediction_data:
        if data.prediction == 0:
            negative_count += 1
        else:
            positive_count += 1

    chart_data = {
        'negativeCount': negative_count,
        'positiveCount': positive_count,
    }

    return JsonResponse(chart_data)

def generate_diabetes_chart_data(request):
    user = request.user
    prediction_data = DiabetesPredictionData.objects.filter(user=user)

    # Count the number of negative and positive predictions
    negative_count = 0
    positive_count = 0

    for data in prediction_data:
        if data.prediction == 0:
            negative_count += 1
        else:
            positive_count += 1

    chart_data = {
        'negativeCount': negative_count,
        'positiveCount': positive_count,
    }

    return JsonResponse(chart_data)

# def improve_health(request):
#     return render(request, 'improve_health.html')



def render_with_improve_health(request, template_name, context=None):
    return render(request, template_name, context)

def improve_health(request):
    return render_with_improve_health(request, 'improve_health.html')

def improve_heart(request):
    return render_with_improve_health(request, 'improve_heart.html')

def improve_diabetes(request):
    return render_with_improve_health(request, 'improve_diabetes.html')


# def render_with_result(request, template_name, context=None):
#     return render(request, template_name, context)
