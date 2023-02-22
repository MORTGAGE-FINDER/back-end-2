from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
import random


class Loans(models.Model):
    county = models.CharField(max_length=256)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    race = models.TextField(blank=True)
    male_female = models.TextField(blank=True)
    age = models.IntegerField(default=0)
    color = models.TextField(blank=True)
    gender = models.TextField(blank=True)

    def __str__(self):
        return self.county

    def save(self, *args, **kwargs):

        if not self.pk and not self.last_name:
            color = self.race
            gender = self.male_female

            age_per_person = [
                int(random.randint(color, gender) * self.age)
                for _ in range(100)
            ]

            self.hourly_sales = age_per_person

        super().save(*args, **kwargs)

