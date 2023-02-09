from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    color = models.CharField(max_length=7, blank=True, null=True)
    def __str__(self):
        return str(self.user.username)

