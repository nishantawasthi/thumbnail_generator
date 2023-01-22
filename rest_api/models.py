from django.db import models


class Thumbnail(models.Model):
    """
    Store all information related to a thumbnail.
    """
    STATUS_CHOICES = [
        (1, 'PENDING'),
        (2, 'SUCCESS'),
        (3, 'FAILED')
    ]

    STATUS_MAP = {
        1: 'PENDING',
        2: 'SUCCESS',
        3: 'FAILED'
    }

    STATUS_MAP_REV = {
        'PENDING': 1,
        'SUCCESS': 2,
        'FAILED': 3
    }

    name = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    status = models.IntegerField(choices=STATUS_CHOICES, null=True)
    task_id = models.CharField(max_length=500, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
