from django.contrib.auth import hashers
from django.shortcuts import render, redirect
import json
from users.models import Users as UserProfile
from users.forms import *
from userprofile.decorators import check_user

def register(request):

    if request.method == 'POST':

        form = RegisterForm(request, request.POST, request.FILES)
        if form.is_valid():
            #Process data in form.clean_data and save to database
            recipients = form.cleaned_data.get('email')
            user = UserProfile(**form.cleaned_data)
            #from django.core.mail import send_mail
            #send_mail('subject', 'message', 'info@zapscms.com', recipients)
            #import pdb; pdb.set_trace()
            try:
                user.save()
            except Exception, e:
                raise e
            return redirect('/')
    else:
        form = RegisterForm(request)

    return render(request, 'users/register.html', {
        'form': form
    })

def login(request):
    user = request.session.get('zapsuser', False)
    if user:
        return redirect('/')


    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            usr = form.get_user()
            sess_user = {
                "first_name": usr.first_name,
                "last_name":  usr.last_name,
                "email":   usr.email,
                "is_active":   usr.is_active,
                #"dob":   usr.birth_date,
                "username":   usr.username,
            }
            request.session['zapsuser'] = json.dumps(sess_user)
            return redirect('/')

    else:
        form = LoginForm()

    return render(request, 'users/login.html', {
        'form': form
    })

@check_user('zapsuser')
def logout(request):
    try:
        del request.session['zapsuser']
    except KeyError:
        pass

    return redirect('/')