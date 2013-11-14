from django.contrib.auth import hashers
from django.shortcuts import render, redirect
from users.models import *
from users.forms import *

def register(request):
    #pas = hashers.make_password('ahsan')
    #import pdb; pdb.set_trace()
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            #Process data in form.clean_data and save to database
            recipients = form.cleaned_data.get('email')
            form.clean_data['password'] = hashers.make_password(form.cleaned_data.get('password'), None, 'md5')
            user = Users(form.cleaned_data)
            from django.core.mail import send_mail
            send_mail('subject', 'message', 'info@zapscms.com', recipients)
            user.save()
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {
        'form': form
    })
