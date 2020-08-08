from django.shortcuts import render
from django.http import HttpResponse
from .models import BudgetItem

def budget(request): 
    budgetItems = BudgetItem.objects.all()
    scoutType = request.GET.get('scoutType')
    return render(request, 'budget/home.html', context={'budgetItems':budgetItems,'scoutType':scoutType})    
