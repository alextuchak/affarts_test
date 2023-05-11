from django.urls import path
from .views import Register

app_name = 'users'

urlpatterns = [
    path('registration/', Register.as_view(), name='registration'),
]