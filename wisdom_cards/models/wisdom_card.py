from django.db import models


class WisdomCard(models.Model):
    section = models.CharField(max_length=50)
    contents = models.TextField()

    class Meta:
        app_label = 'wisdom_cards'
