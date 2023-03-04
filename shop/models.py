from django.db import models

from Utils.ModelUtil import ModelUtil


class Shop(ModelUtil):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=256)
    work_time = models.CharField(max_length=50, default=None, null=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name
