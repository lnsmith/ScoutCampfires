from django.shortcuts import render
from django.http import HttpResponse

def budget(request): 
    scoutType = request.GET.get('scoutType')
    return render(request, 'budget/home.html',{'scoutType':scoutType})
