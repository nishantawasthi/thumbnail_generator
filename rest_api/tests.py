from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from rest_api.utils import check_image, generate_image


class ThumbnailTestCase(APITestCase):
    """
    Contains unit test cases for ThumbnailGenerator view.
    """

    def setUp(self):
        self.image = generate_image()
        self.file = open('test.txt', 'r+')
        self.client = APIClient()
        self.url = '/api/v1/thumbnail_generator/'

    def test_valid_check_image(self):
        """
        Unit test to test check image function for valid input.
        """
        response = check_image(self.image)
        self.assertTrue(response)

    def test_invalid_check_image(self):
        """
        Unit test to test check image function for invalid input.
        """
        response = check_image(self.file)
        self.assertFalse(response)

    def test_generate_image(self):
        """
        Unit test to test generate image function.
        """
        response = check_image(generate_image())
        self.assertTrue(response)

    def test_valid_key_and_value_payload(self):
        """
        Unit test to test successful post request.
        """
        response = self.client.post(self.url, {"image": self.image})
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertTrue('task_id' in response.data)
        self.assertEqual(type(response.data['task_id']), str)

    def test_wrong_or_missing_payload_key(self):
        """
        Unit test to test wrong or missing payload key request.
        """
        response = self.client.post(self.url, {"file": self.image})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('error_code' in response.data)
        self.assertEqual(response.data['error_code'], 400)

    def test_corrupt_or_invalid_image(self):
        """
        Unit test to test corrupt or invalid image request.
        """
        response = self.client.post(self.url, {"image": self.file})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('error_code' in response.data)
        # print(response.data, response, response.data['error_code'])
        self.assertEqual(response.data['error_code'], 400)

    def test_wrong_payload_value(self):
        """
        Unit test to test wrong payload value request.
        """
        response = self.client.post(self.url, {"image": 'test message'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('error_code' in response.data)
        self.assertEqual(response.data['error_code'], 400)
