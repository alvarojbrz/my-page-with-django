from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def criar_usuario(request):
    return HttpResponse('Você criou um usuário!')