from django import forms
from django.contrib.auth import hashers
from datetime import datetime
from users.models import Users

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    gender = forms.CharField(required=False)
    birth_date = forms.DateField(required=True)
    rel_status = forms.CharField(required=False)
    ip_address = forms.IPAddressField(required=False)
    avatar = forms.ImageField(required=False)
    address = forms.CharField(required=False)
    interested_in = forms.CharField(required=False)
    looking_for = forms.CharField(required=False)
    mobile = forms.CharField(required=False)
    is_active = forms.BooleanField(required=False)
    join_date = forms.DateTimeField(required=False)
    updated = forms.DateTimeField(required=False)

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(RegisterForm, self).__init__(*args, **kwargs)

    def clean(self):
        self.cleaned_data['password'] = hashers.make_password(self.cleaned_data.get('password'))
        self.cleaned_data['ip_address'] = self.request.META.get('REMOTE_ADDR')
        self.cleaned_data['join_date'] = datetime.now()
        self.cleaned_data['updated'] = datetime.now()

        if(self.cleaned_data.get('is_active') is False):
            self.cleaned_data['is_active'] = 0
        else:
            self.cleaned_data['is_active'] = 1

        return self.cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user_cache = None

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        try:
            user = Users.objects.get(email__exact=email)
            if not user and hashers.check_password(password,user.password) is False:
                self._errors['password'] = 'Please provide correct email and password'
                forms.ValidationError('Please provide correct email and password.')
            elif user.is_active is False:
                self._errors['inactive'] = 'User is inactive.'
            else:
                self.user_cache = user
        except Users.DoesNotExist:
            pass
        return self.cleaned_data

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache
