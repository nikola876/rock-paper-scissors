from django.urls import path
from . import views
from .views import RegisterView 

urlpatterns = [
    path('', views.game_view, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
]
