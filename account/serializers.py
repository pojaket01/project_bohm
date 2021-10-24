from rest_framework import fields, serializers
from .models import *
from account import models 




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# class ProfileSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Profile
#         fields = '__all__'

# class DegreeSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Degree
#         fields = '__all__'

class FacultySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'

# class User_DegeeSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User_Degee
#         fields = '__all__'