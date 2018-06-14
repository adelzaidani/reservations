from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Role(models.Model):
    role=models.CharField(max_length=30,unique=True)
    def __str__(self):
        return self.role


class Profil(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    role=models.ForeignKey(Role,on_delete=models.CASCADE, default=1)
    language=models.CharField(max_length=2)

    @receiver(post_save, sender=User)
    def update_user_profil(sender,instance,created,**kwargs):
        if created:
            Profil.objects.create(user=instance)
        instance.profil.save()


