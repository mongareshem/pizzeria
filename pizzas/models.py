from django.db import models

class Pizza(models.Model):
    """The different kinds of pizzas."""
    name = models.CharField(max_length=100)

    def __str__(self):
        """Returns the name of the pizzas."""
        return self.name


class Topping(models.Model):
    """Specific toppings used."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        """Returns the specific toppings."""
        return self.name
