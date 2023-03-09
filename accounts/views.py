from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        if len(email) <= 0:
            message.error('Email id field may not be empty')
        if len(password) <= 0:
            message.error('Password field may not be empty')
 
        try:
            username = User.objects.get(email = email).username
        except User.DoesNotExist:
            messages.error(request, "Invalid email id")
            return redirect('login')
            
        if username:
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid password")
                return redirect('login')
        else:
            messages.error(request, "Invalid email id")
            
    return render(request, 'login.html')
