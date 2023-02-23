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
    age = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)
    gender = models.TextField(blank=True)

    def __str__(self):
        return self.county

    # def save(self, *args, **kwargs):
    #
    #     if not self.pk and not self.age:
    #         color = self.race
    #         gender = self.male_female
    #
    #         age_per_person = [
    #             int(random.randint(min, max) * self.age)
    #             for _ in range(100)
    #         ]
    #
    #         self.average_age = age_per_person
    #
    #     super().save(*args, **kwargs)

