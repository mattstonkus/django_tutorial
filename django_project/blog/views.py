from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    returnHttpResponse('<h1>Blog Home</h1>')
