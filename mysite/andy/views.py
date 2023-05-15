from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import login
from django.contrib import messages

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Account
from django.conf import settings

def index(request):
   return render (request, 'home.html')



# class Migration (migrations.Migration)
    
@csrf_exempt
def createAccount(request):
    if request.method == 'POST':
        # Get the data from the POST request
        username = request.POST.get('username')
        password = request.POST.get('password')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')

        # Create a new Account object
        account = Account.objects.create(
            username=username,
            password=password,
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            id = id
        )





