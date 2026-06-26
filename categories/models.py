from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class MainCategory(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Automatically create default categories when a new user registers
DEFAULT_CATEGORIES = {
    'Food & Dining': ['Groceries', 'Restaurants', 'Coffee', 'Snacks'],
    'Shopping': ['Clothing', 'Electronics', 'Accessories', 'Online Shopping'],
    'Transport': ['Fuel', 'Public Transit', 'Taxi', 'Parking'],
    'Entertainment': ['Movies', 'Games', 'Music', 'Sports'],
    'Income': ['Salary', 'Freelance', 'Gift', 'Bonus'],
}

@receiver(post_save, sender=User)
def create_default_categories(sender, instance, created, **kwargs):
    if created:
        for main_name, sub_names in DEFAULT_CATEGORIES.items():
            main = MainCategory.objects.create(name=main_name, user=instance)
            for sub_name in sub_names:
                SubCategory.objects.create(
                    name=sub_name,
                    main_category=main,
                    user=instance  # make absolutely sure user is passed
                )