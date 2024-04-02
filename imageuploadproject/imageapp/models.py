from django.db import models


# Create your models here.
class Card(models.Model):
    card_title = models.CharField(max_length=50)
    card_image = models.FileField(
        upload_to="card_image/", max_length=250, null=True, default=None
    )
