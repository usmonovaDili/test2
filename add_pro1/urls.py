from django.urls import path
from .views import *

urlpatterns = [
    path('', info, name='info_def'),
    path('all/', poll, name='poll_def')
]
