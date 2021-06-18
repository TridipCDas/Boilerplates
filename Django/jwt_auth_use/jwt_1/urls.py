from django.urls import path
from rest_framework_simplejwt import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from . import views

urlpatterns = [
    path('',views.JWTAuth.as_view(),name="jwt-token"),
    path('gettoken/',TokenObtainPairView.as_view(),name="get-token"),
    path('refreshtoken/',TokenRefreshView.as_view(),name="refresh-token"),
    path('verifytoken/',TokenVerifyView.as_view(),name="verify-token")
]