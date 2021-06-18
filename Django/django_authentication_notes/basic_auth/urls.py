from django.urls import path
from . import views

urlpatterns = [
    path('',views.BasicAuth.as_view(),name="basic")
]