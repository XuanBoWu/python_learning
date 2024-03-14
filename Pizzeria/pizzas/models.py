from django.db import models

# Create your models here.
class Pizza(models.Model):
    """ Pizza 数据 """
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Topping(models.Model):
    """ 配料数据 """
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name