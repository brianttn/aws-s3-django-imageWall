from django.urls import path
from . import views

app_name = 'photos'     # Define the Namespace of APP as photos

urlpatterns = [
    path('', views.index, name='Index')
]