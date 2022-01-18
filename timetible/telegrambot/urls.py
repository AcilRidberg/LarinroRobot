from django.urls import path
from .views import *

urlpatterns = [
    path('webhook/', tg_web_hook, name='webhook')
]