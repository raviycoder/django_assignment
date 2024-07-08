from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError

import datetime
from django.contrib.auth.models import User

# Create your views here.

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import User
import datetime

@csrf_exempt
def submit(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        if name and email:  # Ensure name and email are not empty
            try:
                new_user = User.objects.create(name=name, email=email)
                return render(request, 'myapp/submit.html', {'name': name, 'email': email, 'success': True})
            except IntegrityError:
                # Assuming email is unique, handle the error
                return render(request, 'myapp/index.html', {'error': 'Email already exists.'})
    return render(request, 'myapp/index.html')

def home(request):
    return render(request, 'myapp/index.html')

def dynamic(request):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render(request, 'myapp/dynamic.html', {'current_time': current_time})

def users(request):
    users = User.objects.all()
    return render(request, 'myapp/users.html', {'users': users})