from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from .auth import CustomAuthToken

urlpatterns = [
    # path('gettoken/',obtain_auth_token),
    path('',views.StudentModelViewset.as_view(),name="token-1"),
    path('gettoken/',CustomAuthToken.as_view()) #For Custom response while obtaining token.


]