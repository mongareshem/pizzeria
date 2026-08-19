from tkinter.constants import CASCADE

from django.db import models
from django.db.models.fields import TextField


class Pizza(models.Model):
    """The different kinds of pizzas."""
    name = models.CharField(max_length=100)

    def __str__(self):
        """Returns the name of the pizzas."""
        return self.name


class Topping(models.Model):
    """Specific toppings used."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = TextField()

    def __str__(self):
        """Returns the specific toppings."""
        return self.name
