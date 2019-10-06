from django.db import models

# Create your models here.
class User(models.Model):
    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, unique=True)
    email = models.CharField(max_length=128, unique=True)
    passwod = models.CharField(max_length=128, unique=True)

    def __int__(self):
        return self.userId

class Task(models.Model):
    TaskId = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    title = models.CharField(max_length=128)
    date = models.DateTimeField(blank=True, null=True)

    def __int__(self):
        return self.TaskId