from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class CinemaHall(models.Model):
    name = models.CharField(max_length=200)
    total_seats = models.IntegerField(default=100)
    available_seats = models.IntegerField(default=100)

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateTimeField()
    end_date = models.DateTimeField()
    rating = models.IntegerField()
    image_url = models.URLField(max_length=200, blank=True)
    cinemahall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

    
class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seats = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"


