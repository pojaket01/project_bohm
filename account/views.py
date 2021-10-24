from django.db.models.fields import EmailField
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import response, viewsets


from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from account import serializers
from .models import *
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime 


# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        "List":"/task-list/",
        "Detail View":"/task-detail/<str:pk>/",
        "Create":"/task-create/",
        "Update":"/task-update/<str:pk>/",
        "Delete":"/task-delete/<str:pk>/",
    }
    return Response(api_urls)

# class User_detail(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class Degree_Detail(viewsets.ModelViewSet):
#     queryset = Degree.objects.all()
#     serializer_class = DegreeSerializer

# class User_Degee_Detail(viewsets.ModelViewSet):
#     queryset = User_Degee.objects.all()
#     serializer_class = User_DegeeSerializer

class Faculty_Detail(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class LoginView(APIView):
    def post(self, request):
        # email = request.data['email']
        username = request.data['username']
        password = request.data['password']

        user =User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password): 
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret' ,algorithm='HS256')
        
        
        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data ={
            'jwt' : token 
        }
            
        return response

@api_view(['GET'])
def User_data(request):
    data = User.objects.all()
    serializer = UserSerializer(data,many=True)
    return Response(serializer.data)
        


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret' , algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message' : 'success'
        }
        return response