from django.db import models


POSITION = (
    (0, 'SVCNTS'),
    (1, 'Dev 1'),
    (2, 'Dev 2'),
    (3, 'Dev 3')
)


# Create your models here.
class Person(models.Model):
    username = models.CharField(max_length=10, unique=True)
    fullname = models.CharField(max_length=30)
    position = models.IntegerField(choices=POSITION, default=1)


class Project(models.Model):
    name = models.CharField(max_length=20, unique=True)