from django.db import models


class Thumbnail(models.Model):
    """
    Store all information related to a thumbnail.
    """
    name = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
