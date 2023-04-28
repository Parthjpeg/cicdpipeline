from django.contrib import admin
from .models import *

register = [User , event , registerforevents]
admin.site.register(register)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_display = ['id' , 'name', 'price', 'mode', 'address', 'date', 'Modrator', 'Performer','link']
    list_display = ['id' ,'event','Viewer']
# Register your models here.
