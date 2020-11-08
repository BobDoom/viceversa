from django.http import HttpResponse
from django.shortcuts import render

def home_vv(request):
    return render(request, 'home_vv.html')