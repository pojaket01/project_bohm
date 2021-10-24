from django.db.models.fields import EmailField
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import response, viewsets

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

from .models import *
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

# Create your views here.
