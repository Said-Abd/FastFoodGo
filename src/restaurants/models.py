from django.db import models
import uuid

class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ville=  models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
