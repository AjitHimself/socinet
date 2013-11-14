from django import forms
from django.contrib.auth import hashers
from users.models import Users

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    gender = forms.CharField(required=False)
    birth_date = forms.DateField(required=False)
    rel_status = forms.CharField(required=False)
    ip_address = forms.IPAddressField()
    avatar = forms.ImageField(required=False)
    address = forms.CharField(required=False)
    interested_in = forms.CharField(required=False)
    looking_for = forms.CharField(required=False)
    mobile = forms.CharField(required=False)
    is_active = forms.BooleanField(required=False)
    join_date = forms.DateTimeField(required=False)
    updated = forms.DateTimeField(required=False)

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user_cache = None

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        
        user = Users.objects.get(email__exact=email)
        if not user and hashers.check_password(password, 'md5') is False:
            self._errors['password'] = 'Please provide correct email and password' 
            forms.ValidationError('Please provide correct email and password.')
        elif user.is_active is False:
            self._errors['inactive'] = 'User is inactive.' 
        return self.cleaned_data

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache
