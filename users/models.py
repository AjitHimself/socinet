from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=60, unique=True, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=False, db_index=True)
    password = models.CharField(max_length=60)
    gender = models.CharField(max_length=10, blank=True, null=False)
    birth_date = models.DateField(default='0000-00-00')
    rel_status = models.CharField(max_length=120, blank=True)
    ip_address = models.IPAddressField()
    avatar = models.ImageField(upload_to='avatar', blank=True)
    address = models.TextField(blank=True)
    interested_in = models.CharField(max_length=255, blank=True)
    looking_for = models.CharField(max_length=255, blank=True)
    mobile = models.CharField(max_length=40)
    is_active = models.BooleanField(default=0)
    join_date = models.DateTimeField(default='0000-00-00 00:00:00', blank=True)
    updated = models.DateTimeField(default='0000-00-00 00:00:00', blank=True)

    class Meta:
        db_table = 'users'
        app_label = 'users'
        
