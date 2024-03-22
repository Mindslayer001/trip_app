from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Trip(models.Model):
    city = models.CharField(max_length = 50)
    country = models.CharField(max_length = 2)
    start_date = models.DateField()
    end_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "trips")

    def __str__(self):
        return self.city

class Notes(models.Model):
    type_choices = [
        ("dining", "Dinnig"),
        ("eating", "Eating"),
        ("general", "General"),
    ]
    trip = models.ForeignKey(Trip, on_delete = models.CASCADE, related_name = 'trip')
    title = models.CharField(max_length = 100)
    description = models.TextField()
    type = models.CharField(max_length = 100, choices = type_choices)
    image = models.ImageField(upload_to='notes/', blank=True, null=True)
    rating = models.PositiveIntegerField(default = 0, validators = [MaxValueValidator(5)])

    def __str__(self):
        return f"{self.trip.city} | {self.title}"
    
