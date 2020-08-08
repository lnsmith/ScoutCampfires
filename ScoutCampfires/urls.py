from django.contrib import admin
from django.urls import path
from django.conf import settings
import campfire.views as campfire_views 
import budget.views as budget_views

urlpatterns = [
    path('', campfire_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('budget/', budget_views.budget, name='budget'),
    ]
    