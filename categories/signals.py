from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import MainCategory, SubCategory


@receiver(post_save, sender=User)
def create_default_categories(sender, instance, created, **kwargs):
    if created:

        food = MainCategory.objects.create(
            name='Food',
            user=instance
        )

        shopping = MainCategory.objects.create(
            name='Shopping',
            user=instance
        )

        transport = MainCategory.objects.create(
            name='Transport',
            user=instance
        )

        accommodation = MainCategory.objects.create(
            name='Accommodation',
            user=instance
        )

        # Food
        SubCategory.objects.create(name='Breakfast', main_category=food)
        SubCategory.objects.create(name='Lunch', main_category=food)
        SubCategory.objects.create(name='Dinner', main_category=food)

        # Shopping
        SubCategory.objects.create(name='Clothes', main_category=shopping)
        SubCategory.objects.create(name='Electronics', main_category=shopping)
        SubCategory.objects.create(name='Groceries', main_category=shopping)

        # Transport
        SubCategory.objects.create(name='Taxi', main_category=transport)
        SubCategory.objects.create(name='Bus', main_category=transport)
        SubCategory.objects.create(name='Train', main_category=transport)

        # Accommodation
        SubCategory.objects.create(name='Hotel', main_category=accommodation)
        SubCategory.objects.create(name='Rent', main_category=accommodation)
        SubCategory.objects.create(name='Utilities', main_category=accommodation)