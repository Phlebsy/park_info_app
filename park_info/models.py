from django.db import models


class ParkInfo(models.Model):
    title = models.TextField()
    id = models.TextField(primary_key=True)
    description = models.TextField()
    category = models.TextField()
    url = models.TextField()
    parkcode = models.CharField(max_length=4, null=False)
