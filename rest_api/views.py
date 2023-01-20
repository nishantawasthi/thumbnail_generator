from rest_framework.views import APIView


class ThumbnailGenerator(APIView):
    """
    Takes an image as input and resizes it to a given size.
    """

    def post(self, request):
        """Handles post request and resizes it.

        Args:
            request (dict): Store all information of the request
        """
        pass
