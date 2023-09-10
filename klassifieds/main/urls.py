from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path('home/', views.home, name='home'),
]