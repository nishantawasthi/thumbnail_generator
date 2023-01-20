from rest_framework.views import APIView
from rest_framework.response import Response


class ThumbnailGenerator(APIView):
    """
    Takes an image as input and resizes it to a given size.
    """

    def get(self):
        """
        Handles post request and resizes it.

        Args:
            request (dict): Store all information of the request
        """
        return Response('Hello World!')

    def post(self, request):
        """
        Handles post request and resizes it.

        Args:
            request (dict): Store all information of the request
        """
        return Response(request.body)
