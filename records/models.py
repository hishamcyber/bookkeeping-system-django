from django.db import models
from django.contrib.auth.models import User
from categories.models import SubCategory

# Create your models here.
class Record(models.Model):
    TRANSACTION_TYPES = (
        ('income','Income'),
        ('expense','Expense')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"