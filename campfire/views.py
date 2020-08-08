from django.shortcuts import render

def home(request):
    return render(request, 'campfire/home.html')
    