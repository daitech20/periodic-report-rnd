from django.db import models
from django.utils import timezone


POSITION = (
    (0, 'SVCNTS'),
    (1, 'Dev 1'),
    (2, 'Dev 2'),
    (3, 'Dev 3')
)


# Create your models here.
class Employee(models.Model):
    username = models.CharField(max_length=10, unique=True)
    fullname = models.CharField(max_length=30)
    position = models.IntegerField(choices=POSITION, default=1)

    class Meta:
        verbose_name_plural = "Nhân sự"

    def __str__(self) -> str:
        return self.username


class Project(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name_plural = "Dự án"

    def __str__(self) -> str:
        return self.name



class BugStatus(models.Model):
    name = models.CharField(max_length=20, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Bug status"

    def __str__(self) -> str:
        return self.name


class TimeLine(models.Model):
    title = models.CharField(max_length=100, unique=True)
    time = models.DateField(default=timezone.now, unique=True)

    class Meta:
        verbose_name_plural = "Thời gian"

    def __str__(self) -> str:
        return f"{self.title} ({self.time})"