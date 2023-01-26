import traceback

from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_api.errors import InvalidImageError
from rest_api.models import Thumbnail
from rest_api.serializers import ThumbnailSerializer
from rest_api.tasks import resize_image
from rest_api.utils import check_image


class ThumbnailGenerator(APIView):
    """
    Takes an image as input and resizes it to a given size.
    """

    def get(self, request, task_id):
        """
        Handles get request for ThumbnailGenerator view.

        Args:
            request (dict): Contains all information of the request

        Returns:
            Response: Response with message, status and code.
        """
        status_code = status.HTTP_200_OK
        try:
            thumbnail = Thumbnail.objects.filter(task_id=task_id)
            if thumbnail.count():
                thumbnail = thumbnail[0]
                data = {'status': 'success', 'task_id': task_id, 'task_status': Thumbnail.STATUS_MAP[thumbnail.status],
                        'message': ''}
                if Thumbnail.STATUS_MAP[thumbnail.status] == 'PENDING':
                    data['message'] = 'Your image is getting resized please try again after some time.'
                elif Thumbnail.STATUS_MAP[thumbnail.status] == 'FAILED':
                    data['message'] = "Your image's resizing failed please reupload your image and try again."
                else:
                    data['message'] = 'Your image is successfully resized. You can access and download it using the url given below.'
                    serializer = ThumbnailSerializer(
                        thumbnail, context={'request': request})
                    data['image'] = serializer.data
            else:
                status_code = status.HTTP_404_NOT_FOUND
                data = {'status': 'failed', 'task_id': task_id,
                        'message': 'There is no task running or available with this task id please check and confirm your task id and then try again.'}
        except Exception as err:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            data = {'status': 'failed', 'error_code': 500,
                    'message': 'Some unexpected error occurred.'}
            print(err)
            traceback.print_exc()
        return Response(data=data, status=status_code)

    def post(self, request):
        """
        Handles post request for ThumbnailGenerator view.

        Args:
            request (dict): Contains all information of the request

        Returns:
            Response: Response with message, status and code.
        """
        data = None
        status_code = status.HTTP_202_ACCEPTED
        try:
            image = request.FILES['image']
            if not check_image(image):
                raise InvalidImageError
            thumbnail = Thumbnail.objects.create(name=image.name, image=image)
            task = resize_image.delay(thumbnail.id)
            thumbnail.task_id = task
            thumbnail.status = Thumbnail.STATUS_MAP_REV['PENDING']
            thumbnail.save()
            data = {'status': 'success', 'task_id': task.id,
                    'message': 'Your image is getting resized you can retrieve or check status of your image with the task id.'}
        except InvalidImageError as err:
            status_code = status.HTTP_400_BAD_REQUEST
            data = {'status': 'failed', 'error_code': InvalidImageError.error_code,
                    'message': f'{InvalidImageError.error_message} please refer to readme to check your request and try again.'}
            print(err)
            traceback.print_exc()
        except MultiValueDictKeyError as err:
            status_code = status.HTTP_400_BAD_REQUEST
            data = {'status': 'failed', 'error_code': 400,
                    'message': 'Invalid or missing payload data please refer to readme to check your request and try again.'}
            print(err)
            traceback.print_exc()
        except Exception as err:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            data = {'status': 'failed', 'error_code': 500,
                    'message': 'Some unexpected error occurred.'}
            print(err)
            traceback.print_exc()
        return Response(data=data, status=status_code)
