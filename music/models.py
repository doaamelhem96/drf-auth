from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Music(models.Model) :
    name=models.CharField(max_length=255)
    desc=models.TextField(blank=True)
    artist=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    def __str__(self):
        return self.name + " by "+self.artist.username

