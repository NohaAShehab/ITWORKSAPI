from django.db import models


# Create your models here.

class WatchList(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.title}"




class Movie(models.Model):
    name = models.CharField(max_length=100)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="movies",null= True)
    description = models.CharField(max_length=100, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"



