from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    role=models.CharField(max_length=30)

class Profil(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    role=models.ForeignKey(Role,models.DO_NOTHING)
    language=models.CharField(max_length=2)



