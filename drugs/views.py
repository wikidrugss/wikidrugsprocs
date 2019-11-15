from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    return render(request, 'drugs/post_list.html', {})

def infomarihuana(request):
    return render(request, 'drugs/infomarihuana.html', {})    

