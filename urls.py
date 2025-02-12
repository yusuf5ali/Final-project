from django.urls import path
from .views import predict_mpg

urlpatterns = [
    path('', predict_mpg, name='predict_mpg'),
]