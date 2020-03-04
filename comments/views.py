from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the test page.")

def home(request):
    return render(request,'comments/home.html')

def profile(request):
    return

def rank(request):
    return

def work(request):
    return

def result(request):
    return

def post_list(request):
     return render(request, 'comments/post_list.html', {})
