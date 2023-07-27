from django.urls import path
from .views import add_pro,pro_add

urlpatterns=[
    path('',add_pro),
    path('add/',pro_add)
]