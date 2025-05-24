from django.db import models
from django.contrib.auth.models import User

class PlayerScore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}: {self.score}"
