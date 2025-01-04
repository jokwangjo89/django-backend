from django.db import models

class House(models.Model):
    
    """Model definition for Houses"""

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField()
    description = models.TextField() #긴 텍스트 입력
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True)