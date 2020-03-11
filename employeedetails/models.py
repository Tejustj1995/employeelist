from django.db import models

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Employee(models.Model):
    fullname = models.CharField(max_length=30, blank=True)
    empcode = models.CharField(max_length=30, blank=True)
    mobile =models.BigIntegerField(blank=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.empcode