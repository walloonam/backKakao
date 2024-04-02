from django.db import models

from app.models import ShowModel

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=10,null=False, default='')
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)
    admin = models.BooleanField(default=False)

    class Meta:
        app_label = 'user'


class Like(models.Model):
    concert = models.ForeignKey(ShowModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

class Reserve(models.Model):
    concert = models.ForeignKey(ShowModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)



