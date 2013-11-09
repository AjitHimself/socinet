from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=60, unique=True, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=False, db_index=True)
    password = models.CharField(max_length=60)
    gender = models.CharField(max_length=10)
    birth_date = models.DateField()
    rel_status = models.CharField(max_length=120)
    ip_address = models.IPAddressField()
    avatar = models.ImageField(upload_to='avatar')
    adress = models.TextField()
    interested_in = models.CharField(max_length=255)
    looking_for = models.CharField(max_length=255)
    mobile = models.CharField(max_length=40)
    is_active = models.BooleanField()
    join_date = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        db_table = 'users'
        app_label = 'users'
        
