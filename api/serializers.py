from .models import *
from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
 class Meta:
  model = event
  fields = ['id' , 'name', 'price', 'mode', 'address', 'date', 'Modrator', 'Performer','link']

class EventandPerformerSerializer(serializers.ModelSerializer):
 events = EventSerializer(many = True , read_only=True)
 class Meta:
  model = User
  fields = ['id' ,'username','first_name','last_name','email' , 'role' , 'events']

class PerformerSerializer(serializers.ModelSerializer):
 class Meta:
  model = User
  fields = ['id' ,'username','first_name','last_name','email' , 'role']

class RegisterEventSerializer(serializers.ModelSerializer):
 class Meta:
  model = registerforevents
  fields = ['id' ,'event','Viewer']