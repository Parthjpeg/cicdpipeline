from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager


ROLE_CHOICES = (
    ("1", "Viewer"),
    ("2", "Admin"),
    ("3", "Performer"),
    ("4", "Modrator"),
)

MODE = (
    ("1", "Online"),
    ("2", "Offline"),
)

class User(AbstractUser):
    phone_number = models.CharField(max_length=12, unique=True)
    role = models.CharField(max_length = 20,choices = ROLE_CHOICES,default = '1')
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone_number' , 'first_name' , 'last_name' , 'email' , 'role']
    objects = UserManager()

class event(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    mode = models.CharField(max_length = 20,choices = MODE,default = '1')
    address = models.CharField(max_length=100 , null = True)
    date = models.DateTimeField()
    Modrator = models.ForeignKey(User,to_field="username",on_delete=models.CASCADE , null = True  , related_name='Modrator')
    Performer = models.ForeignKey(User,to_field="username",on_delete=models.CASCADE , related_name='events')
    link = models.CharField(max_length=100 , null = True)

class registerforevents(models.Model):
    event = models.ForeignKey(event,to_field="id",on_delete=models.CASCADE)
    Viewer = models.ForeignKey(User,to_field="username",on_delete=models.CASCADE)
# Create your models here.
