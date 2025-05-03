from django.urls import path
from . import views

urlpatterns = [
    path('criar_usuario/', views.criar_usuario)
]