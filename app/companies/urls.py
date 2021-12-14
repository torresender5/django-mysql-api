from django.urls import path
from .views import Company

urlpatterns=[
    path('companies/',  Company.as_view())
]