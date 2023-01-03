from django.db import models

# Create your models here.
class Tag_costs(models.Model):
    name = models.CharField(max_length=25, unique=True, null=False)

    def __str__(self):
        return self.name


class Tag_income(models.Model):
    name = models.CharField(max_length=25, unique=True, null=False)

    def __str__(self):
        return self.name


class MoneyBalance(models.Model):
    money_movement = models.CharField(max_length=25, null=False)
    description = models.CharField(max_length=150, null=False)
    money = models.FloatField(null=False)
    date_of_entry = models.DateField()
    tags_costs = models.ManyToManyField(Tag_costs)
    tags_income = models.ManyToManyField(Tag_income)

    def __str__(self):
        return self.description

