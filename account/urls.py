from django.urls import path
from django.urls.conf import include

from .models import *
from . import views
from .views import LoginView , UserView , LogoutView
from rest_framework import routers

router = routers.DefaultRouter()
# router.register('profile',views.Profile_Detail)
# router.register('degree',views.Degree_Detail)
# router.register('user',views.User_detail)
router.register('faculty',views.Faculty_Detail)


urlpatterns = [
    path('',include(router.urls)),
    path('login/', LoginView.as_view(), name="login",),
    path('user-profile/', UserView.as_view(), name="user-profile",),
    path('logout/', LogoutView.as_view(), name="logout",),
    path('data/', views.User_data, name="logout",)

]
