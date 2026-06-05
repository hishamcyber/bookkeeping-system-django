from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MainCategory(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name