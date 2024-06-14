from django.db import models
from django.contrib.auth.models import User 

class ChatHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    query = models.TextField()
    sim1 = models.FloatField()
    sim2 = models.FloatField()
    sim3 = models.FloatField()
    answer = models.TextField()

    def __str__(self):
        return f"{self.user.username} at {self.datetime}"