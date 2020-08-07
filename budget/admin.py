from django.contrib import admin
from .models import BudgetItem
from .models import BudgetRecord

admin.site.register(BudgetItem) 
admin.site.register(BudgetRecord)
