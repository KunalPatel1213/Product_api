from django.db import models

# Create your models here.


class Details(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    phoneno = models.CharField(max_length=15)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

