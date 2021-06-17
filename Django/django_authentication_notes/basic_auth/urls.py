from django.urls import path
from . import views

urlpatterns = [
    path('basic',views.BasicAuth.as_view(),name="basic")
]