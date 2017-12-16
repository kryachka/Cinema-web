from django.db import models
from django.conf import settings


# Create your models here.
class Profile(models.Model):
    user = models.EmailField(max_length=256)
    name = models.CharField(max_length=128)

    def __str__(self):
        return "%s %s" % (self.user, self.name,)


class Meta:
    verbose_name = 'Profile'
    verbose_name_plural = 'Profiles'
