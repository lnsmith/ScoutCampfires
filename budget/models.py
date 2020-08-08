from django.db import models

class BudgetItem(models.Model):
    objects = models.Manager(
    )
    TypeChoices = [
        ('INC', 'Income'),
        ('EXP', 'Expense'),
    ]
    Type = models.CharField(
        max_length=3,
        choices=TypeChoices,
        default='INC',
    )
    Description = models.CharField(
        max_length=50,
    )


class BudgetRecord(BudgetItem):
    objects = models.Manager(
    )
    Amount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )        
    Date = models.DateTimeField(
        auto_now_add=True,
    )
    
    