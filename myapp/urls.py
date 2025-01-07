from django.urls import path
from .views import *

urlpatterns = [
    path('create-document/', DocumentCreateView.as_view(), name='create-document'),
]
