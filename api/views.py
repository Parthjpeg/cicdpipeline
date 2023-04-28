from rest_framework.decorators import api_view
from rest_framework.response import Response 
from django.shortcuts import render
from rest_framework import status
from .serializers import *
from rest_framework import viewsets
from .models import *
from django.contrib.auth import get_user_model



@api_view(['Post'])
def register(request):
    data = request.data
    if data.get('phone_number') is None:
        return Response({'msg':'Phone Number is required'}, status=status.HTTP_406_NOT_ACCEPTABLE)

    if data.get('password') is None:
        return Response({'msg':'Password is required'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    if data.get('first_name') is None:
        return Response({'msg':'first_name is required'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    if data.get('last_name') is None:
        return Response({'msg':'last_name is required'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    if data.get('email') is None:
        return Response({'msg':'email is required'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    if data.get('role') is None:
        return Response({'msg':'role is required'}, status=status.HTTP_406_NOT_ACCEPTABLE)

    try:
        user = User.objects.create(
            username = data.get('username'),
            phone_number = data.get('phone_number'),
            role = data.get('role'),
            first_name = data.get('first_name'),
            last_name = data.get('last_name'),
            email = data.get('email')
            )
        user.set_password(data.get('password'))
        user.save()
        return Response({'msg':'User Registered'}, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({'msg':'User Not Registered'}, status=status.HTTP_406_NOT_ACCEPTABLE)



@api_view(['POST'])
def login(request): 
    data = request.data 
    if data.get('username') is None:
        return Response({'msg':'User Name is required'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    try:
        user_obj = User.objects.get(username=data.get('username'))
    except Exception as e:
        return Response({'msg':'Invalid Username'}, status=status.HTTP_406_NOT_ACCEPTABLE) 
    
    if user_obj.check_password(data.get('password')):
        return Response({'msg':'Login Successful'}, status=status.HTTP_200_OK)
    
    elif not user_obj.check_password(data.get('password')):
        return Response({'msg':'Please Enter Correct Password'}, status=status.HTTP_406_NOT_ACCEPTABLE)



class EventView(viewsets.ModelViewSet):
  queryset = event.objects.all()
  serializer_class = EventSerializer
  def get_queryset(self):
    if(self.request.data):
        queryset = event.objects.filter(performer=self.request.data.get('performer'))
        return queryset
    else:
        return event.objects.all()
  def post(self,request, *args, **kwargs):
    return self.create(request, *args, **kwargs)



class PerformerView(viewsets.ModelViewSet):
  User = get_user_model()
  queryset = User.objects.filter(role = "3")
  serializer_class = PerformerSerializer



class PerformereventView(viewsets.ModelViewSet):
  User = get_user_model()
  queryset = User.objects.all()
  serializer_class = EventandPerformerSerializer
  def get_queryset(self):
    queryset = User.objects.filter(role = "3" )
    return queryset
  

class RegisterView(viewsets.ModelViewSet):
  queryset = registerforevents.objects.all()
  serializer_class = RegisterEventSerializer
  def get_queryset(self):
    if(self.request.data.get('performer')):
        queryset = registerforevents.objects.filter(Viewer = self.request.data.get('performer'))
        return queryset
    elif(self.request.data.get('event')):
        queryset = registerforevents.objects.filter(event = self.request.data.get('event'))
        return queryset
    elif(self.request.data.get('Viewer')):
        queryset = registerforevents.objects.filter(Viewer = self.request.data.get('Viewer'))
        return queryset
    else:
        return registerforevents.objects.all()
  def post(self,request, *args, **kwargs):
    return self.create(request, *args, **kwargs)