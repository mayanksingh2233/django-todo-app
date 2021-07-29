from django.db import models

# Create your models here.
class contact(models.Model):
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.phone_number


class Todo(models.Model):
    todo_name=models.CharField(max_length=100)
    is_complete = models.BooleanField(default=False)
    