import sys
import traceback

from io import BytesIO
from PIL import Image
from celery import shared_task
from django.core.files.uploadedfile import InMemoryUploadedFile

from rest_api.models import Thumbnail


@shared_task()
def resize_image(thumbnail_id):
    """
    Celery task to resize image and then save it in db.

    Args:
        thumbnail_id (int): Primary key of thumbnail object
    """
    thumbnail = Thumbnail.objects.get(id=thumbnail_id)
    try:
        temp_image = Image.open(thumbnail.image)
        image_format = temp_image.format
        image_mime_type = temp_image.get_format_mimetype()
        # temp_image = temp_image.convert('RGB')
        io_stream = BytesIO()
        temp_image_resized = temp_image.resize((100, 100))
        temp_image_resized.save(io_stream, image_format)
        io_stream.seek(0)
        resized_image = InMemoryUploadedFile(io_stream, 'image',
                                             thumbnail.image.name, image_mime_type,
                                             sys.getsizeof(io_stream), None)
        thumbnail.image = resized_image
        thumbnail.name = resize_image.name
        thumbnail.status = Thumbnail.STATUS_MAP_REV['SUCCESS']
        thumbnail.save()
    except Exception as err:
        thumbnail.status = Thumbnail.STATUS_MAP_REV['FAILED']
        thumbnail.save()
        print(err)
        traceback.print_exc()
