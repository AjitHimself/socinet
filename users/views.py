from django.contrib.auth import hashers
from django.shortcuts import render, redirect
from users.models import Users
from users.forms import *

def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            #Process data in form.clean_data and save to database
            recipients = form.cleaned_data.get('email')
            form.clean_data['password'] = hashers.make_password(form.cleaned_data.get('password'))
            user = Users(form.cleaned_data)
            #from django.core.mail import send_mail
            #send_mail('subject', 'message', 'info@zapscms.com', recipients)
            user.save()
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {
        'form': form
    })

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                u = Users.objects.get(email=request.POST['email'])
                if u.password == hashers.make_password(request.POST['password']):
                    request.session['user'] = u
                    return redirect('/')
            except Users.DoesNotExist:
                pass

    else:
        form = LoginForm()

    return render(request, 'users/login.html', {
        'form': form
    })

def logout(request):
    try:
        del request.session['user']
    except KeyError:
        pass

    return redirect('/')